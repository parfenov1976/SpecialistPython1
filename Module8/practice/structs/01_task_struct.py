# Бегун проводил ежедневные тренировки и записывал расстояния которые пробел за занятия в метрах:
distances = [600, 755, 321.6, 1234, 231, 456.6, 4561, 1200, 456]
# Переведите все значения в футы (получить и вывести новый список)

distances_feet = list(map(lambda x: int(x*3.28), distances))
print('Расстояния в футах:', distances_feet)
