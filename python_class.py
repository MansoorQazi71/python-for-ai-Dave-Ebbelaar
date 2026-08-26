class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def make_sound(self):  # Override parent method
        return f"{self.name} barks: Woof!"

class Cat(Animal):
    def make_sound(self):  # Override parent method
        return f"{self.name} meows: Meow!"

# Different animals, different sounds
generic = Animal(name="Something")
dog = Dog(name="Buddy")
cat = Cat(name="Whiskers")

print(generic.make_sound())  # Something makes a sound
print(dog.make_sound())      # Buddy barks: Woof!
print(cat.make_sound())      # Whiskers meows: Meow!