# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
# Найдите:
print(f"Товары на складе представлены брэндами: ")
set_brand = set()
for n in items:
    set_brand.add(n['brand'])
for n in sorted(set_brand):
    print(n)

print("На складе больше всего товаров брэнда(ов): ")
list_items = []
for n in items:
    list_items.append(n['brand'])
brand_dict = {}
for n in set_brand:
    brand_dict.update([(n, list_items.count(n))])
max_count = sorted(brand_dict.items(), key=lambda x: x[1])[-1][1]
for el in sorted(brand_dict.items(), key=lambda x: x[1]):
    if max_count == el[1]:
        print(el[0])
print(f"По {max_count} ед. каждого.")

print("На складе самый дорогой товар брэнда(ов): ")
price_dict = {}
for n in items:
    price_dict.update([(n['brand'], n['price'])])
max_price = sorted(price_dict.items(), key=lambda x: x[1])[-1][1]
for el in sorted(price_dict.items(), key=lambda x: x[1]):
    if max_price == el[1]:
        print(el[0])
