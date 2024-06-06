"""
Заполните поле для игры Сапёр.

На вход подаются натуральные числа m и n - размеры игрового поля,
затем k - количество мин, далее координаты мин - x и y для каждой мины,
нумерация координат начинается с единицы.

Необходимо вывести на печать игровое поле:

- если в клетке расположена мина, выведите для этой клетки "█";

- если в клетке мины нет, нужно посчитать, сколько мин расположено в
соседних клетках (включая угловые и боковые), и вывести для этой клетки
посчитанное число.

Примечание. Каждая строка оканчивается символом (не пробелом!).
"""

import random


def show_map(field):
    for raw in field:
        raw = list(map(str, raw))
        print(" ".join(raw))


def miner_map(width, height, mines):
    field = [[0 for i in range(width)] for j in range(height)]
    for mine in mines:
        field[mine[0]][mine[1]] = "█"
    show_map(field)
    print("\n")
    for raw in range(height):
        if raw == 0:
            shift_y = [0, 2]
        elif raw != height - 1:
            shift_y = [-1, 2]
        else:
            shift_y = [-1, 1]
        for col in range(width):
            if col == 0:
                shift_x = [0, 2]
            elif col != width - 1:
                shift_x = [-1, 2]
            else:
                shift_x = [-1, 1]
            number = 0
            for i in range(raw + shift_y[0], raw + shift_y[1]):
                for j in range(col + shift_x[0], col + shift_x[1]):
                    if field[i][j] == "█":
                        number += 1
            """scan_field = []
            count_x = 0
            for i in range(raw+shift_y[0], raw+shift_y[1]):
                scan_field.append(list())
                for j in range(col+shift_x[0], col+shift_x[1]):
                    scan_field[count_x].append(field[i][j])
                count_x += 1
            for i in range(len(scan_field)):
                for j in range(len(scan_field[0])):
                    if scan_field[i][j] == '█':
                        number += 1"""
            if field[raw][col] != "█":
                field[raw][col] = number
    show_map(field)


width = 10
height = 2
mines = []
for i in range(6):
    mines.append([random.randint(0, height - 1), random.randint(0, width - 1)])
print("\n")
miner_map(width, height, mines)
print("\n")
