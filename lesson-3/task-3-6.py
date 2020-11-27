# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
# первой буквой. Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием. В программу должна
# попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать
# вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную
# ранее функцию int_func().

get_initcap = lambda str: str.title()


def get_initcap2(str):
    local_str = str
    local_str = str[0].upper() + str[1:len(str)]
    return local_str

initcap_string=""
user_string = input("Введите строку слов с пробелами: ")
for r in user_string.split():
    initcap_string=initcap_string+get_initcap(r)+" "
print(initcap_string)
