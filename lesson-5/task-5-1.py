ffile = open("task-5-1.txt", "w")

while True:
    user_string = input("Введите строку: ")
    if len(user_string) == 0:
        break
    ffile.write(user_string+"\n")
ffile.close()
