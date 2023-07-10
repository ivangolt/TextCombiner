from tkinter import Tk, Button, Label, Entry, filedialog
from docx import Document

def combine_text_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        combined_text = ' '.join([line.strip()[9:-2] for line in lines if line.strip().startswith('"text"')])

    return combined_text

def write_combined_text_to_word_file(combined_text, output_file_path):
    document = Document()
    document.add_paragraph(combined_text)
    document.save(output_file_path)
    status_label.config(text="Объединенный текст сохранен в файл " + output_file_path)

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        selected_file_entry.delete(0, "end")
        selected_file_entry.insert("end", file_path)

def select_output_path():
    output_file_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Files", "*.docx")])
    if output_file_path:
        output_file_entry.delete(0, "end")
        output_file_entry.insert("end", output_file_path)

def combine_and_save():
    file_path = selected_file_entry.get()
    output_file_path = output_file_entry.get()
    if file_path and output_file_path:
        combined_text = combine_text_from_file(file_path)
        write_combined_text_to_word_file(combined_text, output_file_path)

# Создание главного окна
root = Tk()
root.title("Объединение текста в файл Word")

# Метка для выбранного файла
selected_file_label = Label(root, text="Выберите файл .txt:")
selected_file_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Поле для выбранного файла
selected_file_entry = Entry(root, width=50)
selected_file_entry.grid(row=0, column=1, padx=10, pady=10)

# Кнопка для выбора файла
select_file_button = Button(root, text="Выбрать файл", command=select_file)
select_file_button.grid(row=0, column=2, padx=10, pady=10)

# Метка для пути сохранения файла
output_file_label = Label(root, text="Путь для сохранения файла Word (.docx):")
output_file_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Поле для пути сохранения файла
output_file_entry = Entry(root, width=50)
output_file_entry.grid(row=1, column=1, padx=10, pady=10)

# Кнопка для выбора пути сохранения файла
select_output_path_button = Button(root, text="Выбрать путь", command=select_output_path)
select_output_path_button.grid(row=1, column=2, padx=10, pady=10)

# Кнопка для объединения и сохранения
combine_save_button = Button(root, text="Объединить и сохранить", command=combine_and_save)
combine_save_button.grid(row=2, column=1, padx=10, pady=10)

# Метка статуса
status_label = Label(root, text="")
status_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Запуск основного цикла приложения
root.mainloop()
