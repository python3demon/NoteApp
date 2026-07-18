import customtkinter as ctk

WINDOW_TITLE = "Note App"
WINDOW_GEOMETRY = "600x400"
APPEARANCE_MODE = "dark"
COLOR_THEME = "green"

COLOR_SUCCESS = "green"
COLOR_ERROR = "#c22121"


class EasyNoteApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(WINDOW_TITLE)
        self.geometry(WINDOW_GEOMETRY)

        ctk.set_appearance_mode(APPEARANCE_MODE)
        ctk.set_default_color_theme(COLOR_THEME)

        self._notes: dict[str, str] = {"Hello": ""}

        self._configure_grid()
        self._create_widgets()

    def _configure_grid(self) -> None:
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure(1, weight=1)

    def _create_widgets(self) -> None:
        self._title_entry = ctk.CTkEntry(
            self, placeholder_text="Введите название файла..."
        )
        self._menu_options = ctk.CTkOptionMenu(
            master=self, values=list(self._notes.keys()), command=self._on_select_note
        )

        self._text_area = ctk.CTkTextbox(self)
        self._status_label = ctk.CTkLabel(self, text="")

        self._save_button, self._clear_button = (
            ctk.CTkButton(self, text="Сохранить", command=self._save_note),
            ctk.CTkButton(self, text="Очистить", command=self._clear_text),
        )

        # Загаловок, текстовое поле, строка состояние
        self._title_entry.grid(
            row=0, column=0, padx=15, pady=15, sticky="ew", columnspan=2
        )
        self._menu_options.grid(row=0, column=2, padx=15, pady=15, sticky="e")
        self._text_area.grid(
            row=1, column=0, padx=15, pady=5, sticky="nsew", columnspan=3
        )
        self._status_label.grid(
            row=2, column=0, padx=15, pady=5, sticky="ew", columnspan=3
        )

        # Кнопки
        self._save_button.grid(
            row=3, column=0, columnspan=2, sticky="ew", padx=15, pady=15
        )
        self._clear_button.grid(row=3, column=2, sticky="ew", padx=15, pady=15)

    def _save_note(self) -> None:
        title = self._title_entry.get().strip()
        if len(title) < 3:
            self._update_status(
                text="Имя файла должно быть не короче 3 символов!",
                text_color=COLOR_ERROR,
            )
            return

        content = self._text_area.get("1.0", "end-1c")
        self._notes[title] = content

        self._menu_options.configure(values=list(self._notes.keys()))
        self._menu_options.set(title)

        self._update_status(text="Файл успешно сохранен!", text_color=COLOR_SUCCESS)

    def _clear_text(self) -> None:
        self._text_area.delete("1.0", "end")

    def _on_select_note(self, choice: str) -> None:
        self._title_entry.delete(0, "end")
        self._title_entry.insert(0, choice)

        self._text_area.delete("1.0", "end")
        self._text_area.insert("1.0", self._notes[choice])

    def _update_status(self, text: str, text_color: str) -> None:
        self._status_label.configure(text=text, text_color=text_color)


if __name__ == "__main__":
    app = EasyNoteApp()
    app.mainloop()
