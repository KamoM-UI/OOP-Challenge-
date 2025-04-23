
class Pet:
    def __init__(self, name, breed):
        self.name = name 
        self.breed = breed
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = ["jump", "sit"]

    def eat(self):
        self.hunger = min(0, self.hunger + 3)
        self.happiness = max(10, self.happiness + 1)
        print(f"{self.name} eats food!")

    def sleep(self):
        self.energy = max(10, self.energy + 5)
        print(f"{self.name} takes a nap!")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = max(10, self.happiness + 2)
            self.hunger = max(10, self.hunger - 1)
            print(f"{self.name} plays!")
        else:
            print(f"{self.name} is too tired to play.")

    def get_status(self):
        print(f"Status of {self.name}:")
        print(f"  Hunger: {self.hunger}/10")
        print(f"  Energy: {self.energy}/10")
        print(f"  Happiness: {self.happiness}/10")

    def teach_trick(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.happiness = max(10, self.happiness + 2)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows the trick: {trick}.")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} doesn't know any tricks yet.")


my_pet = Pet("Rex", "Rottweiler")
my_pet.eat()
my_pet.sleep()
my_pet.play()
my_pet.teach_trick("roll over")
my_pet.teach_trick("sit")
my_pet.show_tricks()
my_pet.get_status()