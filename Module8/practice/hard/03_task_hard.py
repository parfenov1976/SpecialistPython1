# "Негостеприимные панды"
# В панда парке был очень плохой управляющий. Из-за его ошибок вышло так, что многие клетки с пандами переполнены,
# многие не заполнены, а есть и вовсе пустые. Пришел новый управляющий и захотел решить создавшуюся проблему,
# перераспределив панд по клеткам.

# Но управляющий столкнулся с двумя проблемами:
# Общество защиты животных запретило выселять панд из клеток, если клетка не переполнена;
# Панды оказались не очень-то дружелюбны к новым соседям и больше одного нового соседа не принимают.
# Зато в пустые клетки можно переселять панд из разных клеток.

# Напишите программу, которая определяет сколько панд были "лишними" в своих клетках (суммарное переполнение клеток).
# И какое суммарное переполнение получится, после массового переселения панд.

# Алгоритм переселения нужно разработать самостоятельно с учетом ограничений.

# Формат входных данных
# n - суммарное количество клеток (4 ≤ n ≤ 100)
# Pn - количество панд в каждой клетке (0 ≤ Pn ≤ 10)
# Sn - количество мест в каждой клетке (1 ≤ Sn ≤10)

cells = [[10, 12],
         [8, 6],
         [5, 0],
         [7, 12],
         [12, 8],
         [6, 4]]

print(cells)

extra_pandas = 0

for cell in cells:
    if cell[1] > cell[0]:
        extra_pandas += (cell[1] - cell[0])

while True:
    empty_cells = list(filter(lambda x: x[1] == 0, cells))
    overpop_cells = list(filter(lambda x: x[1] - x[0] > 0, cells))
    if not overpop_cells:
        break
    max_overpop_cell = overpop_cells[0]
    for cell in overpop_cells:
        if cell[1] - cell[0] > max_overpop_cell[1] - max_overpop_cell[0]:
            max_overpop_cell = cell
    if empty_cells:
        for cell in empty_cells:
            relocating_pandas = max(max_overpop_cell[1] - max_overpop_cell[0], cell[0])
            cell[1] += relocating_pandas
            max_overpop_cell[1] -= relocating_pandas
            break
    else:
        break

not_full_cells = list(filter(lambda x: x[1] < x[0], cells))
while not_full_cells:
    cell = not_full_cells.pop()
    overpop_cells = list(filter(lambda x: x[1] - x[0] > 0, cells))
    if overpop_cells:
        cell[1] += 1
        overpop_cells[0][1] -= 1
    else:
        break

extra_pandas_2 = 0

for cell in cells:
    if cell[1] > cell[0]:
        extra_pandas_2 += cell[1] - cell[0]

print(cells)

print('Количество лишних панд  до переселения, всего: ', extra_pandas)

print('Количество лишних панд  после переселения, всего: ', extra_pandas_2)
