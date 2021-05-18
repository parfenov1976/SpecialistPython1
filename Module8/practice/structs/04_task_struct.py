# Даны два словаря:
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
# Объедините их в один

# 1v
# new_dict = {}
# new_dict.update(dictionary_1)
# new_dict.update(dictionary_2)
# print(new_dict)

# 2v
# new_dict = {**dictionary_1, **dictionary_2}
# print(new_dict)

# 3v - new
d3 = dictionary_1 | dictionary_2
print(d3)
