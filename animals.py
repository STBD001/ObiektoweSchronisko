class Animal:
    def __init__(self, name, age, race):
        self.name = name
        self.age = age
        self.race = race

    def walk(self):
        print(f"Your {self.race}, {self.name}, went for a walk.")

    def feeding(self):
        print(f"Your {self.race}, {self.name}, wants to eat something.")

    def adopted(self):
        print(f"Your {self.race}, {self.name}, was adopted!!")

class Dog(Animal):
    def __init__(self, name, age, race, energy_level):
        super().__init__(name, age, race)
        self.energy_lvl = energy_level

    def bark(self):
        print(f"{self.name} is barking! Woof!")

    def walk(self):
        self.energy_lvl -= 1
        print(f"{self.name} went for a walk and now has energy level {self.energy_lvl}.")

class Cat(Animal):
    def __init__(self, name, age, race, nap_time):
        super().__init__(name, age, race)
        self.nap_time = nap_time

    def purr(self):
        print(f"{self.name} is purring! Purrrr...")

    def nap(self):
        print(f"{self.name} wants to eat and then nap for {self.nap_time} hours.")

def alive_animals():
    puszek = Dog('Puszek', 10, 'Maltese', 15)
    print('Name: ', puszek.name)
    print('Age: ', puszek.age)
    print('Race: ', puszek.race)
    print('Energy Level: ', puszek.energy_lvl)
    puszek.bark()
    puszek.walk()
    print('Energy Level: ', puszek.energy_lvl)
    print("------------------------------------------------------------------")
    mmruczek=Cat('Mruczek', 12, 'Siamese', 2)
    print('Name: ', mmruczek.name)
    print('age: ',mmruczek.age)
    print('Race: ', mmruczek.race)
    mmruczek.purr()
    mmruczek.nap()
    print("------------------------------------------------------------------")