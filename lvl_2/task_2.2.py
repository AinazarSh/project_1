# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

import pymorphy2

def quarter_of(month, num):
    for dict_key, dict_value in month.items():
        morph = pymorphy2.MorphAnalyzer()
        quarter = morph.parse(dict_key)[0]
        gent = quarter.inflect({'gent'})
        for value_key, value_value in dict_value.items():
            if num == value_key:
                return f'Месяц {num} - {value_value} является частью {gent.word} квартала'


dict_of_quarters = {"Первый": {1: "Январь",
                               2: "Февраль",
                               3: "Март"},
                    "Второй": {4: "Апрель",
                               5: "Май",
                               6: "Июнь"},
                    "Третий": {7: "Июль",
                               8: "Август",
                               9: "Сентябрь"},
                    "Четвертый": {10: "Октябрь",
                                  11: "Ноябрь",
                                  12: "Декабрь"},
                    }

quarter_num = int(input('Введите номер месяца: '))

if quarter_of(dict_of_quarters, quarter_num) == None:
    print('Такого месяца нет!')
else:
    print(quarter_of(dict_of_quarters, quarter_num))