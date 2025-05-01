my_dict = {}

my_dict['tuple'] = (42, 13, 5, 90, 2)
print(my_dict['tuple'][-1])

my_dict['list'] = [None, 23, True, 45, 80, 31]
my_dict['list'].append(True)
my_dict['list'].pop(1)
# print(my_dict['list'])

my_dict['dict'] = {'one': 'value1', 'two': None, 'three': 42, 'four': 'value2', 'five': 30}
my_dict['dict'][('i am a tuple',)] = True
my_dict['dict'].pop('two')

# print(my_dict['dict'])

my_dict['set'] = {44, False, 32, 'text1', 43}
my_dict['set'].add(56)
my_dict['set'].remove(44)
# print(my_dict['set'])

print(my_dict)
