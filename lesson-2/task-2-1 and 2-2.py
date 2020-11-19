# ###  TASK 2-1 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа
# данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у
# пользователя, а указать явно, в программе. 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
# сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().


user_list = []
i = 0
print("Введите элементы списка. Пустой элемент = окончание ввода")
while 1 == 1:
    user_element = input(f"Введите элемент {i}: ")
    try:
        user_element = int(user_element)
    except:
        try:
            user_element = float(user_element)
        except:
            user_element=user_element

    # if user_element.isdigit():
    #     user_element = int(user_element)
    if not user_element:
        break
    user_list.append(user_element)
    i += 1
print("Веденные элементы и их тип:")
i = 0
for r in user_list:
    print(f"{i}: ", r, type(r))
    i += 1
print("Введенный список: ",user_list)

### TASK 2-2

index = 0
i=0
if i < len(user_list)//2:
    print("Производим обмен значений соседних элементов")
    while i < len(user_list)//2:
        print("Меняем: ",user_list[index]," и ",user_list[index+1])
        user_list.insert(index, user_list.pop(index + 1))
        index = index + 2
        i+=1
    print("Список после перестановки: ",user_list)
else:
    print("Нет эдементов для перестановки")