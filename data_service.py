"""модуль для роботи з файлами даниих
- зчитування та вивід на екран
"""


def get_dovidnyk():
    """ Повертає дані довідника, який отримує ззовні

    Returns:
        dani_dovidnyka: дані довідника
    """

    
    from_file = [
        "1;Універсам 22",
        "2;Дніпрянка",
        "3;Універсам 23"
    ]

    # накопичувач клієнтів
    dani_dovidnyka = []

    for line in from_file: 
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

    for client in dovidnyk:
        if client_code_from <= client[0] <= client_code_to:
            print("Код підприємства: {} Назва: {}".format(client[0], client[1]))


dovidnyk = get_dovidnyk()   
show_dovidnyk(dovidnyk)



def get_osnovni_pokaznyky():
    """ Повертає дані основних показнкиів, який отримує ззовні

    Returns:
        dani_osnovnyh_pokaznykiv: дані основних показників
    """

    
    from_file = [
        "1;базовий;79280,5;1815,5;7054,0",
        "2;базовий;832714,5;45810,5;17868,0",
        "1;попередній;486088,8;32013,0;37245,0",
        "2;попередній;1665429,0;91621,0;35736,0",
        "1;поточний;464588,0;25584,0;50913,0",
        "2;поточний;2861819,0;89378,0;52783,0",
        "3;базовий;79280,5;1815,5;7054,0",
        "3;попередній;486088,8;32013,0;37245,0",
        "3;поточний;464588,0;25584,0;50913,0"
    ]

    # накопичувач клієнтів
    dani_osnovnyh_pokaznykiv = []

    for line in from_file: 
        line_list = line.split(';')
        dani_osnovnyh_pokaznykiv.append(line_list)

    
    return dani_osnovnyh_pokaznykiv

def show_osnovni_pokaznyky(osnovni_pokaznyky):
    """ Виводить на екран список показників заданого діапазона

    Args:
        osnovni_pokaznyky ([list]): основні показники
    """
  
    client_code_from = input("З якого кода показників? ")
    client_code_to   = input("По який код показників? ")

    for client in osnovni_pokaznyky:
        if client_code_from <= client[0] <= client_code_to:
            print("Код підприємства: {} Період: {:11} Товарообіг: {:10} Прибуток: {:7} Середньорічна вартість осн. засобів: {:7} ".format(client[0], client[1], client[2], client[3], client[4]))


osnovni_pokaznyky = get_osnovni_pokaznyky()   
show_osnovni_pokaznyky(osnovni_pokaznyky)