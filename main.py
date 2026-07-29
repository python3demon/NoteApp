import customtkinter as ctk
from tkinter import filedialog

WINDOW_TITLE = "Note App"
WINDOW_GEOMETRY = "600x400"
APPEARANCE_MODE = "dark"
COLOR_THEME = "green"

COLOR_SUCCESS = "green"
COLOR_ERROR = "#c22121"
BG_HEADER = "#212121"
BG_TEXTAREA = "#0d0d0d"

class NoteManager:
    def __init__(self) -> None:
        self.current_file = ""
        
    def get_content(self) -> None:
        with open(self.current_file, "r") as file:
            file_content = file.read()
        return file_content

    def edit_note(self, content) -> None:
        with open(self.current_file, "w") as file:
            file.write(content)

    def open_file_dialog(self) -> str:
        file_path = filedialog.askopenfilename(
            title="Выберите файл",
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
        )
        return file_path
    
class EasyNoteApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(WINDOW_TITLE)
        self.geometry(WINDOW_GEOMETRY)

        ctk.set_appearance_mode(APPEARANCE_MODE)
        ctk.set_default_color_theme(COLOR_THEME)

        self._manager = NoteManager()

        self._configure_grid()
        self._create_widgets()

    def _configure_grid(self) -> None:
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

    def _create_widgets(self) -> None:
        self._header_frame = ctk.CTkFrame(self, height=48, corner_radius=0, fg_color=BG_HEADER)
        self._header_frame.grid(row=0, column=0, sticky="ew")
        
        self.open_option_menu = ctk.CTkButton(
            self._header_frame,
            text="Open",
            command=self._open_file,
            width=72,
            fg_color="transparent"
        )
        self.open_option_menu.grid(row=0, column=0, padx=12, pady=4)

        self._text_area = ctk.CTkTextbox(self, corner_radius=0, fg_color=BG_TEXTAREA)
        self._text_area.grid(row=1, column=0, sticky="nsew")

    def _open_file(self, choice: str = "Hello") -> None:
        file_path = self._manager.open_file_dialog()
        if not file_path:
            return
        self._manager.current_file = file_path
        file_content = self._manager.get_content()

        self._clear_text()
        self._text_area.insert("1.0", file_content)
        self._manager.current_file = file_path
    
    def _clear_text(self) -> None:
        self._text_area.delete("1.0", "end")

if __name__ == "__main__":
    app = EasyNoteApp()
    app.mainloop()
