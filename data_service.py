"""модуль для роботи з файлами даниих
- зчитування та вивід на екран
"""


def get_dovidnyk():
    """ Повертає дані довідника, які отримує з файлу "dovidnyk.txt"

    Returns:
        dani_dovidnyka: дані довідника
    """

    
    with open("./data/dovidnyk.txt") as dovidnyk_file:
        from_file = dovidnyk_file.readlines()

    # накопичувач клієнтів
    dani_dovidnyka = []

    for line in from_file: 
        #відрізати '\n' в кінці рядка
        line = line[:-2]
        line_list = line.split(';')
        dani_dovidnyka.append(line_list)

    
    return dani_dovidnyka

def show_dovidnyk(dovidnyk):
    """ Виводить на екран список чогось заданого діапазона

    Args:
        dovidnyk ([list]): довідник
    """
  
    client_code_from = input("З якого кода довідника? ")
    client_code_to   = input("По який код довідника? ")

    kol_lines = 0
    
    for client in dovidnyk:
        if client_code_from <= client[0] <= client_code_to:
            print("Код підприємства: {} Назва: {}".format(client[0], client[1]))
            kol_lines += 1

    if kol_lines == 0:
        print("Не існує")

dovidnyk = get_dovidnyk()   
show_dovidnyk(dovidnyk)



def get_osnovni_pokaznyky():
    """ Повертає дані основних показнкиів, який отримує з "osnovni_pokaznyky.txt"

    Returns:
        dani_osnovnyh_pokaznykiv: дані основних показників
    """

    
    with open("./data/osnovni_pokaznyky.txt") as pokaznyky_file:
        from_file = pokaznyky_file.readlines()

    # накопичувач клієнтів
    dani_osnovnyh_pokaznykiv = []

    for line in from_file: 
        #відрізати '\n' в кінці рядка
        line = line[:-2]
        line_list = line.split(';')
        dani_osnovnyh_pokaznykiv.append(line_list)

    
    return dani_osnovnyh_pokaznykiv

def show_osnovni_pokaznyky(osnovni_pokaznyky):
    """ Виводить на екран список показників 

    Args:
        osnovni_pokaznyky ([list]): основні показники
    """
  
    client_code_from = input("З якого кода показників? ")
    client_code_to   = input("По який код показників? ")

    kol_lines = 0

    for client in osnovni_pokaznyky:
        if client_code_from <= client[0] <= client_code_to:
            print("Код підприємства: {} Період: {:11} Товарообіг: {:10} Прибуток: {:7} Середньорічна вартість осн. засобів: {:7} ".format(client[0], client[1], client[2], client[3], client[4]))
            kol_lines += 1
    if kol_lines == 0:
        print("Не існує")

osnovni_pokaznyky = get_osnovni_pokaznyky()   
show_osnovni_pokaznyky(osnovni_pokaznyky)