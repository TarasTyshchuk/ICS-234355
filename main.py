"""головний модуль задачі
   - виводить на екран та в файл розрахункову таблицю
   - виводить на екран первинні файли
"""

import os
import data_service, process_data
from process_data import create_analiz
from data_service import show_dovidnyk, show_osnovni_pokaznyky, get_dovidnyk, get_osnovni_pokaznyky

MAIN_MENU = \
"""
~~~~~~~~~ ОБРОБКА ОСНОВНИХ ПОКАЗНИКІВ ~~~~~~~~~

1 - вивід показників на екран
2 - запис результату в файл
3 - вивід списку довідника
4 - вивід списку показників
0 - завершення роботи

------------------------------------------------
"""

TITLE = "АНАЛІЗ ОСНОВИХ ПОКАЗНИКІВ ПІДПРИЄМСТВА"

HEADER = \
"""
=============================================================================================================================================================
 Назва показ. | Од. виміру | Підприємство | Баз. рік | Поперед. рік | Поточ. рік | Абсолют. відхил.(+) | Відхил.(+) в % | Абсолют. відхил(-) | Відхил(-) в % 
=============================================================================================================================================================
"""

FOOTER = \
"""
=============================================================================================================================================================

"""

STOP_MASSAGE = "Для продовження натисніть <Enter>"

def show_analiz_table(index_list):
    """вивід на екран таблиці показників
    """
    print(f"\n\n{TITLE:^157}")
    print(HEADER)

    for index in index_list:
        print(f"{index['index_name']:25}",
              f"{index['unit']:5}", 
              f"{index['org']:14}",  
              f"{index['basic_year']:>11}",
              f"{index['pre_year']:>11}",
              f"{index['curr_year']:>11}",
              f"{index['deviation +']:>12.2f}",
              f"{index['+ in percent']:>6.2f}",
              f"{index['deviation -']:>12.2f}",
              f"{index['- in percent']:>4.2f}"
              )
    print(FOOTER)

def write_analiz(index_list):
    """запис аналізу в файл
    """
    with open('./data/analiz.txt', "w") as analiz_file:
        for index in index_list:
            line = index['index_name'] + ';' + \
            index['unit'] + ';' + \
            index['org'] + ';' + \
            str(index['basic_year']) + ';' + \
            str(index['pre_year']) + ';' + \
            str(index['curr_year']) + ';' + \
            str(index['deviation +']) + ';' + \
            str(index['+ in percent']) + ';' + \
            str(index['deviation -']) + ';' + \
            str(index['- in percent']) + '\n'

            analiz_file.write(line)
    
    print("Файл успішно сформовано ...")     


while True:

    os.system('clear')
    print(MAIN_MENU)
    command_number = input("Введіть номер команди: ")

    # обробка команд користувача
    if command_number == '0':
        print('\nПрограма завершила роботу')
        exit(0)

    elif command_number == '1':
        index_list = create_analiz()
        show_analiz_table(index_list)
        input(STOP_MASSAGE)

    elif command_number == '2':
        index_list = create_analiz()
        write_analiz(index_list)
        input(STOP_MASSAGE)

    elif command_number == '3':
        dovidnyk = get_dovidnyk()
        show_dovidnyk(dovidnyk)
        input(STOP_MASSAGE)

    elif command_number == '4':
        osnovni_pokaznyky = get_osnovni_pokaznyky()
        show_osnovni_pokaznyky(osnovni_pokaznyky)
        input(STOP_MASSAGE)   