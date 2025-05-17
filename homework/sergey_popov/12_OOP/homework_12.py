class Flowers:
    stebel = True
    flower = True

    def __init__(self, name, time_life, color, length_stebel, coast):
        self.name = name
        self.time_life = time_life
        self.color = color
        self.length_stebel = length_stebel
        self.coast = coast


class FlowersYellow(Flowers):

    def __init__(self, name, time_life, color, length_stebel, coast):
        super().__init__(name, time_life, color, length_stebel, coast)


class FlowersOrange(Flowers):

    def __init__(self, name, time_life, color, length_stebel, coast):
        super().__init__(name, time_life, color, length_stebel, coast)


class FlowersGreen(Flowers):

    def __init__(self, name, time_life, color, length_stebel, coast):
        super().__init__(name, time_life, color, length_stebel, coast)


flower_1 = FlowersYellow('Подсолнух', 22, 'yellow', 60, 300)
flower_2 = FlowersYellow('Нарцисс', 14, 'yellow', 20, 500)
flower_3 = FlowersOrange('Георгин', 10, 'orange', 25, 700)
flower_4 = FlowersOrange('Герань', 40, 'orange', 10, 350)
flower_5 = FlowersGreen('Гвоздика', 25, 'green', 27, 150)
flower_6 = FlowersGreen('Гортензия', 14, 'green', 30, 250)


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
                print(f'{flower.name} - {getattr(flower, attr, value)}')


new_bouquet = Bouquet(flower_1, flower_2, flower_3, flower_4, flower_5, flower_6)
new_bouquet.bouquet_coast()
new_bouquet.time_death()
new_bouquet.sort_flower('coast')
new_bouquet.search_flower('color', 'green')
