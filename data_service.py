"""модуль для роботи з файлами даниих
- зчитування та вивід на екран
"""


def get_dovidnyk():
    """ Повертає дані довідника, які отримує з файлу "dovidnyk.txt"

    Returns:
        dani_dovidnyka: дані довідника
    """

    
    with open("./data/dovidnyk.txt", encoding="utf-8") as dovidnyk_file:
        from_file = dovidnyk_file.readlines()

    # накопичувач клієнтів
    dani_dovidnyka = []

    for line in from_file: 
        #відрізати '\n' в кінці рядка
        
        line_list = line.split(';')
        dani_dovidnyka.append(line_list)

    
    return dani_dovidnyka

def show_dovidnyk(dovidnyk):
    """ Виводить на екран список довідник показників підприємства за заданим кодом

    Args:
        dovidnyk ([list]): довідник
    """
  
    nazva_pokaznyka_code = input("Введіть код довідника: ")

    kol_lines = 0
    
    for nazva_pokaznyka in dovidnyk:
        if nazva_pokaznyka_code == nazva_pokaznyka[0]:
            print("Код показника: {:4} Назва показника: {:25} Одиниця виміру: {:5}".format(nazva_pokaznyka[0], nazva_pokaznyka[1], nazva_pokaznyka[2]))
            kol_lines += 1

    if kol_lines == 0:
        print("Не існує")

dovidnyk = get_dovidnyk()   
# show_dovidnyk(dovidnyk)



def get_osnovni_pokaznyky():
    """ Повертає дані основних показнкиів, який отримує з "osnovni_pokaznyky.txt"

    Returns:
        dani_osnovnyh_pokaznykiv: дані основних показників
    """

    
    with open("./data/osnovni_pokaznyky.txt", encoding="utf-8") as pokaznyky_file:
        from_file = pokaznyky_file.readlines()

    # накопичувач клієнтів
    dani_osnovnyh_pokaznykiv = []

    for line in from_file: 
        #відрізати '\n' в кінці рядка
        
        line_list = line.split(';')
        dani_osnovnyh_pokaznykiv.append(line_list)

    
    return dani_osnovnyh_pokaznykiv

def show_osnovni_pokaznyky(osnovni_pokaznyky):
    """ Виводить на екран список основних показників діяльності підприємства по заданому коду

    Args:
        osnovni_pokaznyky ([list]): основні показники
    """
  
    pokaznyk_code = input("Введіть код показника: ")

    kol_lines = 0

    for pokaznyk in osnovni_pokaznyky:
        if pokaznyk_code == pokaznyk[1]:
            print("Підприємство: {:14}; Код показника: {:4}; Базовий рік: {:11}; Попередній рік: {:11}; Поточний рік: {}; ".format(pokaznyk[0], pokaznyk[1], pokaznyk[2], pokaznyk[3], pokaznyk[4]))
            kol_lines += 1
    if kol_lines == 0:
        print("Не існує")

osnovni_pokaznyky = get_osnovni_pokaznyky()   
# show_osnovni_pokaznyky(osnovni_pokaznyky)