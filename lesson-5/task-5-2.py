# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.\

ffile = open("task-5-2.txt", "r", encoding="utf-8")
counter_lines = 0
lines = []
for r in ffile:
    counter_lines += 1
    lines.append((counter_lines, len(r.split())))
ffile.close()
print(lines)
