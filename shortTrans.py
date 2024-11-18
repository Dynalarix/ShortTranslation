import tkinter as tk


from googletrans import Translator

def translate_textToRu():
    # Получаем текст из поля ввода
    input_text = text_input.get("1.0", tk.END).strip()
    result_text.delete("1.0", tk.END)  # Очищаем поле результата

    if input_text:
        translator = Translator()
        translated = translator.translate(input_text, dest='ru')

        # Получаем текст после 'text='
        translated_text = str(translated.text)

        # Выводим результат
        result_text.insert(tk.END, f"{translated_text}")
    else:
        result_text.insert(tk.END, "Введите текст для перевода.")


def translate_textToEng():
    # Получаем текст из поля ввода
    input_text = text_input.get("1.0", tk.END).strip()
    result_text.delete("1.0", tk.END)  # Очищаем поле результата

    if input_text:
        translator = Translator()
        translated = translator.translate(input_text, dest='en')

        # Получаем текст после 'text='
        translated_text = str(translated.text)

        # Выводим результат
        result_text.insert(tk.END, f"{translated_text}")
    else:
        result_text.insert(tk.END, "Введите текст для перевода.")


# Создание основного окна
root = tk.Tk()
root.title("Переводчик")
#Black Theme
root.configure(bg='#292628')

# Метка для ввода текста
label_input = tk.Label(root, bg='#292628',fg='white', text="Введите текст для перевода:")
label_input.pack()

# Поле для ввода текста
text_input = tk.Text(root, height=7, width=50, bg='#383838', fg='white', insertbackground='white')
text_input.pack()


# def is_english(text):
#     for i in text:
#         if i in alf_en:
#             return True
#     return False

# Кнопки для перевода
alf_en = 'qwertyuiopsadfghjklzxcvbnm'
translate_buttonRU = tk.Button(root, width=12, bg='#4b4e59', fg='white', text="EN -> RU", command=translate_textToRu)
translate_buttonEN = tk.Button(root, width=12, bg='#4b4e59', fg='white', text="RU -> EN", command=translate_textToEng)
translate_buttonRU.place(x=4, y=154)
translate_buttonEN.place(x=275, y=154)
# if is_english(text_input.get("1.0", tk.END).strip()) == True:
#     translate_buttonRU = tk.Button(root, width=40, bg='#4b4e59', fg='white', text="EN -> RU", command=translate_textToRu)
# elif is_english(text_input.get("1.0", tk.END).strip()) == False:
#     translate_buttonEN = tk.Button(root, width=40, bg='#4b4e59', fg='white', text="RU -> EN", command=translate_textToEng)
# translate_button = tk.Button(root, width=40, bg='#4b4e59', fg='white', text="EN -> RU", command=translate_textToRu)
# translate_button.pack()

# Метка для результата перевода
label_result = tk.Label(root, bg='#292628', fg='white', text="Результат перевода:", pady=12)
label_result.pack()

# Поле для вывода результата
result_text = tk.Text(root, bg='#383838', fg='white', insertbackground='white', height=7, width=50)
result_text.pack()

# Запуск основного цикла приложения
root.mainloop()
