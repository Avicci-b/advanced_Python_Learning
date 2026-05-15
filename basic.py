class Animal:
    is_breathing = True

    def __init__(self, name, age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"The animal's name is {self.name} and it is {self.age} years young"
    
    def animal_Sound(self, sound):
        return f"weeee"
    
class Dog(Animal):
    def animal_Sound(self, sound):
        return f"iiiii"
d1=Dog("Mathew",5)
print(d1.animal_Sound("Helolo"))
a1=Animal("Rabbit",3)
print(a1.animal_Sound("Elolo"))