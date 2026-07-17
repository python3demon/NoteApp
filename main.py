import customtkinter as ctk

window = ctk.CTk()
window.title("Note App")
window.geometry("600x400")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

def save_func():
    title = zagalovok.get()
    print(title)
    if len(title) < 3 or not title.isalnum():
        status.configure(text="Имя файла должно быть не короче 3 символов!", text_color="#c22121")
        return

    option[title] = text.get("0.0", "end")
    optionmenu.configure(values=list(option.keys()))
    status.configure(text="Файл успешно сохранен!", text_color="green")
    
def clear_func():
    text.delete("0.0", "end")

def on_select(choice):
    # Очистка поля для ввода названия и установка название файла
    zagalovok.delete(0, "end")
    zagalovok.insert(0, choice)
    # Очистка TextBoxa и установка текста из файла choice + .txt
    text.delete("0.0","end")
    text.insert("0.0", option[choice])

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=0)
window.grid_columnconfigure(2, weight=0)
window.grid_rowconfigure(1, weight=1)

option = {"Hello":""}

zagalovok = ctk.CTkEntry(window, placeholder_text="Введите название нового файла...")
optionmenu = ctk.CTkOptionMenu(master=window, values=list(option.keys()), command=on_select)

text = ctk.CTkTextbox(window)
status = ctk.CTkLabel(window, text="")

save, clear = (
    ctk.CTkButton(window, text="Сохранить", command=save_func),
    ctk.CTkButton(window, text="Очистить", command=clear_func)
)

# Загаловок, текстовое поле, строка состояние
zagalovok.grid(row=0, column=0, padx=15, pady=15, sticky="ew", columnspan=2)
optionmenu.grid(row=0, column=2, padx=15, pady=15, sticky="e")
text.grid(row=1, column=0, padx=15, pady=5, sticky="nsew", columnspan=3)
status.grid(row=2, column=0, padx=15, pady=5, sticky="ew", columnspan=3)

# Кнопки
save.grid(row=3, column=0, columnspan=2, sticky="ew", padx=15, pady=15)
clear.grid(row=3, column=2, sticky="ew", padx=15, pady=15)


window.mainloop()