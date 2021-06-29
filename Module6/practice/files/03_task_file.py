# Кассовый аппарат был доработан, теперь он пишет не только цены, но и тип проданных товаров.
# Файл data/items_sold.txt - продажи всех товаров за день.
# Каждая строка файла - покупка одного покупателя.
# Узнайте:
# 1. Какова общая выручка магазина
# 2. Какова выручка магазина по каждому типу товаров
# 3. Какой тип товара был продан на самую большую сумму
# 4. Сколько различных типов товаров было продано за день

f = open("data/items_sold.txt", "r", encoding="utf-8")

items_dict = {}
for line in f:
    items_list = line.split()
    for item in items_list:
        pair = item.split(":")
        if items_dict.get(pair[0]) is not None:
            items_dict[pair[0]] += float(pair[1])
        else:
            items_dict[pair[0]] = float(pair[1])

print(items_dict)
print(sum(items_dict.values()))

for key, value in items_dict.items():
    print(f"{key} : {value:.2f}")

max_item = 0
max_item_type = ""
for key, value in items_dict.items():
    if value > max_item:
        max_item = value
        max_item_type = key
print(max_item_type)
print("Различных товаров продано:", len(items_dict))
