class NotDigitErr(Exception):
    def __init__(self):
        print("Ошибка!! Введено не число!! ")


def check_for_digit(element):
    res = False
    check_list=["1","2","3","4","5","6","7","8","9","0","-","."]
    list_check = list(set(element)-set(check_list))
    try:
        if not len(list_check) == 0:
            raise NotDigitErr
        else:
            if element.isdigit():
                res=int(element)
            else:
                res=float(element)
    except NotDigitErr:
        pass
    return res

user_list=[]
while True:
    x = input("Введите число (q для выхода): ")
    if x == 'q':
        break
    x = check_for_digit(x)
    if x:
        user_list.append(x)
print("Получившийся список: ", user_list)
