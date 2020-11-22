# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.\

ffile = open("task-5-2.txt", "r", encoding="utf-8")
counter_lines = 0
counter_symbols = 0
lines = []
for r in ffile:
    counter_lines += 1
    counter_symbols = 0
    for j in list(r):
        counter_symbols += 1
    lines.append((counter_lines, counter_symbols))
ffile.close()
print(lines)
