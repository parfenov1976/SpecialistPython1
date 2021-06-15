# Дано общее количество объектов для отображения на веб-сайте и количество объектов на каждой странице.
# Вычислите, сколько объектов будет отображаться на последней странице сайта.


def pagination(num_items, items_on_page):
    return num_items % items_on_page or items_on_page


print(pagination(245, 5))
print(pagination(125, 10))
print(pagination(19, 10))
print(pagination(117, 20))
