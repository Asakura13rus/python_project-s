my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print("Dict: ", my_dict)
print("Existing value: ", my_dict['Masha'])
print("Not existing value: ", my_dict.get('Kamila'))
my_dict.update(
    {
    'Kamila' : 1981,
    'Artem' : 1915
    }
)
a = my_dict.pop('Artem')
print("Deleted value: ",a)
print("Modified dictionary: ",my_dict)
my_set = {1, 'Яблоко', 42.314, 1, 'Яблоко'}
print("Set: ",my_set)
my_set.add(((5, 6, 1.6)))
my_set.add(13)
my_set.remove(13)
print("Modified set: ",my_set)