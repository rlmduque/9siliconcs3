class Animal:
    def __init__(self, name):
        self._name = name
        
    def eat(self):
        return f"{self._name}, is eating."
        
    def make_sound(self):
        return f"{self._name} makes a sound."
        
class Lion(Animal):
    
    def make_sound(self):
        return f"{self._name} roars loudly!"
    def eat(self):
        return f"{self._name} eats fresh meat."
        
class Elephant(Animal):
    def make_sound(self):
        return f"{self._name} trumpets!"
    def eat(self):
        return f"{self._name} eats grass and fruits"
        
class Monkey(Animal):
    def make_sound(self):
        return f"{self._name} chatters!"
    def eat(self):
        return f"{self._name} eats bananas."
        
lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

print(lion.make_sound())
print(lion.eat())
print("-----")

print(elephant.make_sound())
print(elephant.eat())
print("-----")

print(monkey.make_sound())
print(monkey.eat())
print("-----")
