from tkinter import filedialog

import customtkinter as ctk

WINDOW_TITLE = "Note App"
WINDOW_GEOMETRY = "600x400"
APPEARANCE_MODE = "dark"
COLOR_THEME = "green"

COLOR_SUCCESS = "green"
COLOR_ERROR = "#c22121"
BG_HEADER = "#212121"
BG_TEXTAREA = "#0d0d0d"

FILE_LABEL_FONT = "Courier New"
FILE_LABEL_SIZE = 14


class NoteManager:
    def __init__(self) -> None:
        # Список путей ко всем открытым файлам (вкладкам)
        self.open_files: list[str] = []
        self.active_index: int = -1

    def get_content(self) -> str:
        with open(self.open_files[self.active_index], "r") as file:
            file_content = file.read()
        return file_content

    def edit_note(self, content: str) -> None:
        with open(self.open_files[self.active_index], "w") as file:
            file.write(content)

    def open_file_dialog(self) -> str:
        """Возвращает путь к выбранному файлу.
        В случае нажатия кнопки отмены возвращается пустая строка.
        """
        file_path = filedialog.askopenfilename(
            title="Выберите файл",
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")],
        )
        return file_path

    def save_file_dialog(self) -> str:
        file_path = filedialog.asksaveasfilename(
            title="Сохранить файл как",
            defaultextension=".txt",
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")],
        )
        return file_path


class EasyNoteApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(WINDOW_TITLE)
        self.geometry(WINDOW_GEOMETRY)

        ctk.set_appearance_mode(APPEARANCE_MODE)
        ctk.set_default_color_theme(COLOR_THEME)

        self.bind("<Control-s>", self._save_file)

        self._manager = NoteManager()

        self._configure_grid()
        self._create_widgets()

    def _configure_grid(self) -> None:
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)

    def _create_widgets(self) -> None:
        self._header_frame = ctk.CTkFrame(
            self, height=48, corner_radius=0, fg_color=BG_HEADER
        )
        self._header_frame.grid_columnconfigure(0, weight=0)
        self._header_frame.grid_columnconfigure(1, weight=1)
        self._header_frame.grid(row=0, column=0, sticky="ew")

        self._file_selection_frame = ctk.CTkFrame(
            self, height=48, corner_radius=0, fg_color=BG_HEADER
        )
        self._file_selection_frame.grid(row=1, column=0, sticky="ew")

        self._open_file_button = ctk.CTkButton(
            self._header_frame,
            text="Open",
            command=self._open_file,
            width=72,
            fg_color="transparent",
        )
        self._open_file_button.grid(row=0, column=0, padx=12, pady=4)

        self._file_label = ctk.CTkLabel(
            self._header_frame,
            text="• Новый файл",
            font=(FILE_LABEL_FONT, FILE_LABEL_SIZE, "bold"),
        )
        self._file_label.grid(row=0, column=1, padx=28, pady=4, sticky="e")

        self._text_area = ctk.CTkTextbox(self, corner_radius=0, fg_color=BG_TEXTAREA)
        self._text_area.grid(row=2, column=0, sticky="nsew")

    def _open_file(self) -> None:
        file_path = self._manager.open_file_dialog()  # User chose file
        if not file_path:
            return
        self._manager.open_files.append(file_path)
        self._manager.active_index += 1
        file_content = self._manager.get_content()

        self._clear_text()
        self._file_label.configure(text=f"{file_path.split('/')[-1]}")
        self._text_area.insert("1.0", file_content)
        self._manager.open_files.append(file_path)
        self._manager.active_index += 1
        button_file = ctk.CTkButton(
            self._file_selection_frame,
            text=f"{file_path.split('/')[-1]}",
            command=self._open_file,
            corner_radius=5,
        )
        button_file.grid(row=0, column=self._manager.active_index-1, padx=4, pady=4, sticky="ew")

    def _clear_text(self) -> None:
        self._text_area.delete("1.0", "end")

    def _save_file(self, event=None) -> None:
        # Запрашиваем у пользователя путь если нет открытого файла для сохранения и проверяем, что выбор сделан
        if self._manager.active_index == -1:
            file_path = self._manager.save_file_dialog()
            if not file_path:
                return

            self._manager.open_files.append(file_path)
            self._manager.active_index += 1

            self._file_label.configure(text=f"{file_path.split('/')[-1]}")

        new_content = self._text_area.get("1.0", "end")
        self._manager.edit_note(new_content)


if __name__ == "__main__":
    app = EasyNoteApp()
    app.mainloop()
