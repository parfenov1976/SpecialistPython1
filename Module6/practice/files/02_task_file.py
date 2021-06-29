# Кассовый аппарат пишет цены всех проданных товаров в текстовый файл, наименование проданных товаров не имеет значение.
# По окончанию рабочего дня имеем файл data/sold.txt.
# Узнайте:
# 1. На какую сумму было продано товаров
# 2. Цену самого дорогого товара
# 3. Цену самого дешевого товара

f = open("data/sold.txt", "r", encoding="utf-8")

goods_str = []
goods_float = []
for line in f:
    goods_str += line.split()
print(goods_str)

for good in goods_str:
    goods_float.append(float(good))

print(goods_float)

print("sum = ", sum(goods_float))
print("max = ", max(goods_float))
print("max = ", min(goods_float))
