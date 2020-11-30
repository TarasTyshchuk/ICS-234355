"""головний модуль задачі
- виводить на екран та в файл розразункову таблицю
- виводить на екран первинні файли
"""

import os
from process_data import create_zajavka
from data_service import show_orders, show_clients, get_orders, get_clients

MAIN_MENU = \
"""
~~~~~~~~~ ОБРОБКА ЗАЯВОК НА ПРОДАЖ УСТАТКУВАННЯ  ~~~~~~~~~

1 - вивід заявок на екран
2 - запис результата в файл
3 - вивід списка накладних
4 - вивід списка клієнтів
0 - завершення роботи
--------------------------
"""

TITLE = "ЗАЯВКА НА ПРОДАЖ УСТАТКУВАННЯ ПО МАГАЗИНУ"

HEADER = \
"""
===========================================================================================
  Устаткування     |  Клієнт          | Номер заказа | Кількість |  Ціна     |  Сума   
===========================================================================================
"""

FOOTER = \
"""
===========================================================================================

"""

STOP_MESSAGE = "Для продовження натисніть <Enter>"

def show_zajavka_table(zajavka_list):
    """вивід на екран таблиці заявок
    """
    print(f"\n\n{TITLE:^92}")
    print(HEADER)
    
    for zajavka in zajavka_list:
        print(f"{zajavka['oborud']:20}",
              f"{zajavka['client']:20}",
              f"{zajavka['zakaz']}",
              f"{zajavka['kol']:>14}",
              f"{zajavka['price']:>15.2f}",
              f"{zajavka['total']:>13.2f}",
              )

    print(FOOTER)
    
def write_zajvka(zajavka_list):
    """ запис заявок в файл
    """  
    with open('./data/zajavka.txt', "w") as zajavka_file:
        for zajavka in zajavka_list:
            line =  zajavka['oborud'] + ';' +        \
                    zajavka['client'] + ';' +         \
                    zajavka['zakaz'] + ';' +          \
                    str(zajavka['kol']) + ';' +       \
                    str(zajavka['price']) + ';' +      \
                    str(zajavka['total']) + '\n'       

            zajavka_file.write(line)
            
    print("Файл  успішно сформовано ...")
    
    
while True:
    
    os.system('clear')
    print(MAIN_MENU)
    command_number = input("Введіть номер команди: ")
    
    # обробка команд користувача
    if command_number == '0':
        print('\nПрограмма завершила роботу')
        exit(0)
        
    elif command_number == '1':
        zajavka_list = create_zajavka()
        show_zajavka_table(zajavka_list)
        input(STOP_MESSAGE)
        
    elif command_number == '2':
        zajavka_list = create_zajavka()
        write_zajvka(zajavka_list)
        input(STOP_MESSAGE)
        
    elif command_number == '3':
        orders = get_orders()
        show_orders(orders)
        input(STOP_MESSAGE)
        
    elif command_number == '4':
        clients = get_clients()
        show_clients(clients)
        input(STOP_MESSAGE)


    
