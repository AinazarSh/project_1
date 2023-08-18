# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)
from pprint import pprint

class Matrix:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.matrix = []

    def show_matrix(self):
        for i in range(self.row):
            self.matrix.append([])
            for _ in range(self.col):
                self.matrix[i].append(None)
        return self.matrix

    def change_position(self, row, col, change):
        self.matrix[row][col] = change
        return self.matrix

    def change_element(self, old, new):
        for i,  row in enumerate(self.matrix):
            for j, num in enumerate(row):
                if old == num:
                    self.matrix[i][j] = new
        return self.matrix


matrix = Matrix(10, 10)
pprint(matrix.show_matrix())

print("\nИзменение матрицы с выбором позиции:")
matrix.change_position(row=7, col=5, change=34)
matrix.change_position(row=3, col=5, change=355)
pprint(matrix.matrix)

print("\nИзменение матрицы с выбором элемента:")
matrix.change_element(old=34, new=456)
matrix.change_element(old=None, new=0)
pprint(matrix.matrix)

print(f'\nЧисло строк {matrix.row}, число столбцов {matrix.col}')

