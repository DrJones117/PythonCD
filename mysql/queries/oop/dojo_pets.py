class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, treats, pet_food, pet):

        self.first = first_name
        self.last = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        print("Walking the Dog.")
        self.pet.play()
        return self
    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        print("Here you go.")
        self.pet.eat()
        return self
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        print("Scrubbing")
        self.pet.noise()
        return self


class Pet:
    # implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks):

        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 200

    
    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy + 25
        return self
    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy + 5
        self.health + 10
        return self
    # play() - increases the pet's health by 5
    def play(self):
        self.health + 5
        return self
    # noise() - prints out the pet's sound
    def noise(self):
        print("Rough!!")
        return self


pet1 = Pet("Doug", "German Shepherd", "Sit")
ninja1 = Ninja("Judah", "Kahler", "Bacon", "Kibble", pet1)

ninja1.feed().walk().bathe()
