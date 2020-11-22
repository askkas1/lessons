ffile = open("task-5-3.txt")
list_20k = []
n_lines = 0
n_all_salary = 0
for lines in ffile:
    words = lines.split()
    if len(words) == 0:
        break
    try:
        n_salary = float(words[1])
    except:
        print(f"Некорректная сумма у фамилии: {words[0]}")
        n_salary = 0
    n_all_salary += n_salary
    n_lines += 1
    if n_salary < 20000 and not n_salary == 0:
        list_20k.append(words[0])
ffile.close()
print(list_20k)
n_avg_salary = round(n_all_salary / n_lines, 2)
print(n_avg_salary)
