# Доработайте предыдущую программу так, чтобы каждый сгенерированный сотрудник
# был уникальным(не должны повторяться комбинации Имя + Фамилия).

from random import randint

names = ["Алексей", "Иван", "Александр", "Борис", "Бронислав", "Василий", "Игнат",
         "Григорий", "Дмитрий", "Егор", "Евгений", "Клим", "Кирилл", "Леонид", "Михаил", "Максим", "Николай"]
surnames = ["Алексеев", "Андреев", "Брагин", "Бочкин", "Вескин", "Варенин", "Григораш", "Климов", "Якин",
            "Ложкин", "Колпин", "Минский", "Николаев", "Орешкин", "Петров", "Иванов", "Тяпкин"]
profession = ["инженер", "бетонщик", "сварщик", "такелажник", "охранник", "бухгалтер", "прораб"]
list_size = input('Введите размер списка: ')
emp_list = []
tmp = []
i = 0
while i < int(list_size):
    name = names[randint(1, len(names) - 1)]
    surname = surnames[randint(1, len(surnames) - 1)]
    if f'{name} {surname}' not in tmp:
        i += 1
        tmp.append(f'{name} {surname}')
        emp_list.append({'Имя': name, 'Фамилия': surname, 'Возраст': str(randint(18, 65)),
                         'Профессия': profession[randint(1, len(profession) - 1)], 'Зарплата': randint(10000, 50000)})
emp_list = sorted(emp_list, key=lambda y: y.get('Имя'))
emp_list = sorted(emp_list, key=lambda x: x.get('Фамилия'))
for el in emp_list:
    print(el)
