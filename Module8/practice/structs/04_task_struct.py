# Даны два словаря:
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
# Объедините их в один
new_dict = {}
new_dict.update(dictionary_1)
new_dict.update(dictionary_2)
print(new_dict)
