class Flowers:
    stebel = True
    flower = True

    def __init__(self, name, time_life, color, length_stebel, coast):
        self.name = name
        self.time_life = time_life
        self.color = color
        self.length_stebel = length_stebel
        self.coast = coast

    def __str__(self):
        return f'flower - {self.name}'

    def __repr__(self):
        return f'flower - {self.name}'


class FlowersYellow(Flowers):
    color = 'yellow'

    def __init__(self, name, time_life, length_stebel, coast):
        super().__init__(name, time_life, self.color, length_stebel, coast)


class FlowersOrange(Flowers):
    color = 'orange'

    def __init__(self, name, time_life, length_stebel, coast):
        super().__init__(name, time_life, self.color, length_stebel, coast)


class FlowersGreen(Flowers):
    color = 'green'

    def __init__(self, name, time_life, length_stebel, coast):
        super().__init__(name, time_life, self.color, length_stebel, coast)


flower_1 = FlowersYellow('Подсолнух', 22, 60, 300)
flower_2 = FlowersYellow('Нарцисс', 14, 20, 500)
flower_3 = FlowersOrange('Георгин', 10, 25, 700)
flower_4 = FlowersOrange('Герань', 40, 10, 350)
flower_5 = FlowersGreen('Гвоздика', 25, 27, 150)
flower_6 = FlowersGreen('Гортензия', 14, 30, 250)


class Bouquet:

    def __init__(self, *bouquet_list):
        self.bouquet_list = list(bouquet_list)

    def bouquet_coast(self):
        print(sum(flower.coast for flower in self.bouquet_list))

    def time_death(self):
        print(sum(flower.time_life for flower in self.bouquet_list) / len(self.bouquet_list))

    def sort_flower(self, attr):
        self.bouquet_list.sort(key=lambda flower: getattr(flower, attr))
        for flower in self.bouquet_list:
            print(f'{flower.name} - {getattr(flower, attr)}')

    def search_flower(self, attr, value):
        for flower in self.bouquet_list:
            if getattr(flower, attr) == value:
                return flower
        return None


new_bouquet = Bouquet(flower_1, flower_2, flower_3, flower_4, flower_5, flower_6)
new_bouquet.bouquet_coast()
new_bouquet.time_death()
new_bouquet.sort_flower('coast')
print(new_bouquet.search_flower('time_life', 40))
