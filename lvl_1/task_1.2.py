# Задача 1.2.
# Пункт A.
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
import datetime
import random

def format_times(number):
    seconds = (int(number) * 60) + int(round(((number - int(number)) * 100), 2))
    return seconds

def all_time_songs(collection_of_songs):
    all_time = 0

    if isinstance(collection_of_songs, list):
        for num in range(3):
            all_time += format_times(random.choice(collection_of_songs)[1])
    elif isinstance(collection_of_songs, dict):
        for num in range(3):
            all_time += format_times(random.choice(list(collection_of_songs.values())))

    return round(all_time, 2)

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
# Пункт B.
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

time_timedelta = str(all_time_songs(my_favorite_songs)).split(".")
print(f"Три песни из списка звучат {datetime.timedelta(seconds=all_time_songs(my_favorite_songs))} минут\n"
      f"Три песни из словаря звучат {datetime.timedelta(seconds=all_time_songs(my_favorite_songs_dict))} минут")

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

