from animals import Animal
from animals import Dog
from animals import Cat
class Schelter:
    def __init__(self):
        self.animals=[]

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} has been added to the shelter")

    def adopt_pet(self, name):
        for zwierze in self.animals:
            if zwierze.name == name:
                self.animals.remove(zwierze)
                print(f"{zwierze.name} has been adopted.")
                return
        print(f"An animal named {name} not found.")

    def show_pet(self):
        if not self.animals:
            print("There are no animals in the shelter.")
        else:
            print("Animals in the shelter:")
            for zwierze in self.animals:
                print(f"Name: {zwierze.name}, Age: {zwierze.age}, Race: {zwierze.race}")
def test():
    schronisko=Schelter()
    puszek=Dog('Puszek', 10, 'Maltese', 15)
    mruczek=Cat('Mruczek', 12, 'Siamese', 2)

    schronisko.add_animal(puszek)
    schronisko.add_animal(mruczek)
    schronisko.show_pet()
    print("------------------------------------------------------------------")
    schronisko.adopt_pet('Puszek')
    schronisko.show_pet()