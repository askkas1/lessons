# Создать (не программно) текстовый файл со следующим содержимым: One — 1 Two — 2 Three — 3 Four — 4 Необходимо
# написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

words_dict = {"one": "Один", "two": "Два", "three": "Три", "four": "Четыре"}

ffile_new = open("task-5-4-rus.txt", "w", encoding="utf-8")
with open("task-5-4.txt", "r", encoding="utf-8") as ffile:
    for line in ffile:
        file_string = line.split()
        try:
            print(words_dict.get(file_string.pop(0).lower()) + " " + " ".join(file_string), file=ffile_new)
        except:
            print(f"Некорректная строка: {' '.join(line.split())}", file=ffile_new)
ffile_new.close()
