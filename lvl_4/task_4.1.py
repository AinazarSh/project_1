# Задача 4.1.
# Домашнее задание на SQL
import sqlite3
# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

def get_connection():
  connection = sqlite3.connect("teatchers.db")
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_student():
  try:
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Students(
        Student_Id INTEGER NOT NULL,
        Student_Name TEXT NOT NULL,
        School_Id INTEGER NOT NULL PRIMARY KEY);''')
    connection.commit()
    cursor.execute('''INSERT INTO Students (Student_Id, Student_Name, School_Id)
        VALUES 
        (201, 'Иван', 1),
        (202, 'Петр', 2),
        (203, 'Анастасия', 3),
        (204, 'Игорь', 4);''')
    connection.commit()
    close_connection(connection)
  except(Exception, sqlite3.Error) as error:
    print('Ошибка получения данных', error)

#get_student()

def info_student(student_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(f'''SELECT * FROM Students JOIN School ON School.School_Id = Students.School_Id WHERE Students.Student_Id = {student_id};''')
    result = cursor.fetchall()
    print(f'Вывод данных\n'
          f'ID Студента: {result[0][0]}\n'
          f'Имя студента: {result[0][1]}\n'
          f'ID школы: {result[0][2]}\n'
          f'Название школы: {result[0][4]}')
  except(Exception, sqlite3.Error) as error:
    print('Ошибка получения данных', error)

info_student(203)