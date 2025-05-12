PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_list = PRICE_LIST.splitlines()
new_list1 = [x.rstrip('р') for x in new_list]
new_list2 = [x.split(' ', 1) for x in new_list1]
new_dict = dict(new_list2)
new_dict1 = {x: int(y) for x, y in new_list2}

print(new_dict1)
