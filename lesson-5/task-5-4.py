words_dict = {"one": "Один", "two": "Два", "three": "Три", "four": "Четыре"}
# ffile = open("task-5-4.txt", "r")
# ffile_new = open("task-5-4-rus.txt", "w")
# for r in ffile:
#     if len(r) == 0:
#         break
#     str = r.split()
#     new_string = []
#     new_string.append(words_dict.get(str.pop(0).lower()))
#     new_string.insert(str)
#     new_string.append('\n')
#     ffile_new.writelines(new_string)
#
# ffile.close()
# ffile_new.close()
ffile_new = open("task-5-4-rus.txt", "w")
with open("task-5-4.txt", "r") as ffile:
    for line in ffile.split():
        print(words_dict.get(line.pop(0).lower())+" ".join(line),file=ffile_new)
ffile_new.close()