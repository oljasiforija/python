class Ninja():
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    

@classmethod


class Pet():
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 0 
        self.health = 0
    def sleep(self):
        if self.energy <= 0:
            print(f"{self.name} is sleeping")
        else:
            self.energy += 25
            print(f"{self.name} is active")
    def play(self):
        self.energy += 5
        print(f"{self.name} is playing")
    def eat(self):
        self.health += 5
        self.energy += 5
        print(f"{self.name} increased health and energy")
    def noise(self):
        if self.type == self.type:
            print(f"{self.name} is barking")
        else:
            print(f"{self.name} is meowing")
        

pet1 = Pet('Happy', 'dog', 'sit')
pet2 = Pet('Bella', 'cat', 'chill')
pet3 = Pet('Groot', 'dog', 'spin')


ninja1 = Ninja('John', 'Malkovich', pet1, 'dentastix', 'rice and meat')
ninja2 = Ninja('Anne', 'Johnson', pet2, 'greenies', 'chicken')
ninja1 = Ninja('Mark', 'Doe', pet3, 'bacon', 'turkey')

pet2.noise()
pet3.noise()




