""" аналіз основних показників діяльності підприєств
"""
from data_service import get_dovidnyk, get_osnovni_pokaznyky

# cловник в якому будуть накопичуватись результати розрахунків
index = {
    'index_name'  : '',      #назва показника
    'unit'        : '',      #одиниця виміру
    'org'         : '',      #підприємство
    'basic_year'  : 0.0,     #базовий рік
    'pre_year'    : 0.0,     #попередній рік
    'curr_year'   : 0.0,     #поточний рік
    'deviation +' : 0.0,     #абсолютне відхилення +
    '+ in percent': 0.0,     #абсолютне відхилення + у відсотках
    'deviation -' : 0.0,     #абсолютне відхилення -
    '- in percent': 0.0      #абсолютне відхилення - у відсотках
}

def create_analiz():
    """формування списку даних аналізу основних показників
    діяльності підприємтсва
    
    Returns:
        indexes_list: список даних
    """

    def get_index_name(index_name_code):
        """знаходить назву показники по коду

        Args:
            index_name_code ([type]): код назви показника
        
        Returns:
            [type]: назву показників
        """

        for index_name in dovidnyk:
            if index_name_code == index_name[0]:
                return (index_name[1])
        
        return "*** назва показника не знайдена"

    def get_unit(unit_code):
        """знаходить одиницю виміру по коду

        Args:
            unit_code ([type]): код одиниці виміру
        
        Returns:
            [type]: одиницю виміру   
        """
        
        for unit in dovidnyk:
            if unit_code == unit[0]:
                return (unit[2])
        
        return "*** одиниця виміру не знайдена"

    # накопичувач результатів
    index_list = []
    
    dovidnyk = get_dovidnyk()
    osnovni_pokaznyky = get_osnovni_pokaznyky()

    for pokaznyk in osnovni_pokaznyky:

        # робоча копія
        index_work = index.copy()

        index_work['org']           = pokaznyk[0]
        index_work['basic_year']    = pokaznyk[2]
        index_work['pre_year']      = pokaznyk[3]
        index_work['curr_year']     = pokaznyk[4]
        index_work['deviation +']   = float(index_work['curr_year']) - float(index_work['basic_year'])
        index_work['+ in percent']  = float(index_work['curr_year']) % float(index_work['basic_year'])
        index_work['deviation -']   = float(index_work['curr_year']) - float(index_work['pre_year'])
        index_work['- in percent']  = float(index_work['curr_year']) % float(index_work['pre_year'])
        index_work['index_name']    = get_index_name(pokaznyk[0])
        index_work['unit']          = get_unit(pokaznyk[0])

    return index_list

indexes = create_analiz()
for item in indexes:
    print(item)