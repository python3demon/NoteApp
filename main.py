import customtkinter as ctk

class EasyNoteApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Note App")
        self.geometry("600x400")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure(1, weight=1)

        self.create_widgets()

    def create_widgets(self):
        self.option = {"Hello":""}
        
        self.zagalovok = ctk.CTkEntry(self, placeholder_text="Введите название нового файла...")
        self.optionmenu = ctk.CTkOptionMenu(master=self, values=list(self.option.keys()), command=self.on_select)
        
        self.text = ctk.CTkTextbox(self)
        self.status = ctk.CTkLabel(self, text="")
        
        self.save, self.clear = (
            ctk.CTkButton(self, text="Сохранить", command=self.save_func),
            ctk.CTkButton(self, text="Очистить", command=self.clear_func)
        )
        
        # Загаловок, текстовое поле, строка состояние
        self.zagalovok.grid(row=0, column=0, padx=15, pady=15, sticky="ew", columnspan=2)
        self.optionmenu.grid(row=0, column=2, padx=15, pady=15, sticky="e")
        self.text.grid(row=1, column=0, padx=15, pady=5, sticky="nsew", columnspan=3)
        self.status.grid(row=2, column=0, padx=15, pady=5, sticky="ew", columnspan=3)

        # Кнопки
        self.save.grid(row=3, column=0, columnspan=2, sticky="ew", padx=15, pady=15)
        self.clear.grid(row=3, column=2, sticky="ew", padx=15, pady=15)

    def save_func(self):
        title = self.zagalovok.get()
        if len(title) < 3 or not title.isalnum():
            self.status.configure(text="Имя файла должно быть не короче 3 символов!", text_color="#c22121")
            return
    
        self.option[title] = self.text.get("0.0", "end")
        self.optionmenu.configure(values=list(self.option.keys()))
        self.status.configure(text="Файл успешно сохранен!", text_color="green")
        
    def clear_func(self):
        self.text.delete("0.0", "end")
    
    def on_select(self, choice):
        # Очистка поля для ввода названия и установка название файла
        self.zagalovok.delete(0, "end")
        self.zagalovok.insert(0, choice)
        # Очистка TextBoxa и установка текста из файла choice + .txt
        self.text.delete("0.0","end")
        self.text.insert("0.0", self.option[choice])

if __name__ == "__main__":
    app = EasyNoteApp()
    app.mainloop()
