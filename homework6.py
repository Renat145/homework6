my_dict = {'Ivan': 1985, 'Sasha': 1986, 'Petr': 1987}
print(my_dict)
print(my_dict.get('Ivan'))
print(my_dict.get('Max'))
my_dict.update({'Alex': 1988, 'Inna': 1989})
print(my_dict)
a = my_dict.pop('Petr')
print(a)
print(my_dict)

my_set = {1, 2, 3, 'Urban', False, (1, 2, 3), 1, 2, 3}
print(my_set)
print(my_set.add('Барсик'))
print(my_set.add('Лунтик'))
print(my_set.discard(False))
print(my_set)