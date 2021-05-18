# Данные о сотрудниках в программе хранятся в словаре
staff = [
    {
        'name': 'Алексей',
        'surname': 'Петров',
        'salary': 124300
    },
    {
        'name': 'Николай',
        'surname': 'Петров',
        'salary': 120000
    },
    {
        'name': 'Иван',
        'surname': 'Павлов',
        'salary': 34500
    },
    {
        'name': 'Василий',
        'surname': 'Кукушкин',
        'salary': 162500
    },
    {
        'name': 'Василий',
        'surname': 'Павлов',
        'salary': 47800
    },
]
# Вычислите:
print("Имя и Фамилию сотрудника с самой высокой зарплатой:")
max_salary_emp = staff[0]
max_salary = 0
for emp in staff:
    if int(emp['salary']) > max_salary_emp['salary']:
        max_salary_emp = emp
print(f"{max_salary_emp['name']} {max_salary_emp['surname']}")

print("Имя и Фамилию сотрудника с самой низкой зарплатой:")
min_salary_emp = staff[0]
min_salary = 0
for emp in staff:
    if int(emp['salary']) < min_salary_emp['salary']:
        min_salary_emp = emp
print(f"{min_salary_emp['name']} {min_salary_emp['surname']}")

print("Среднеарифметическую зарплату всех сотрудников")
sum_salary = 0
c = 0
for emp in staff:
    sum_salary = sum_salary + int(emp['salary'])
    c += 1
print(sum_salary / c)

print("Количество однофамильцев в организации")
staff_copy = staff.copy()
namesake_list = []
while True:
    record = staff_copy.pop(0)
    c = 0
    flag = 0
    while c < len(staff_copy):
        if record['surname'] == staff_copy[c]['surname']:
            namesake_list.append(staff_copy.pop(c))
            c -= 1
            flag += 1
        c += 1
    if flag > 0:
        namesake_list.append(record)
    if len(staff_copy) == 0:
        break
print(len(namesake_list))

print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")
staff_dict = {}
for emp in staff:
    a = (emp['name']+" "+emp['surname']), (emp['salary'])
    staff_dict.update([a])
sorted_staff = sorted(staff_dict.items(), key=lambda x: x[1])
for n in sorted_staff:
    print(*n)
