# Classes, objects and instantiating

# How to create class
# Synatx: class name_of_class starting with Capital letter
# good naming convention is required

# classes are a way to bring data and functionality together
class Dog:


    def __init__(self, name, colour): # Initialising Dog class
        # self refers to fido. so essentially, fido.name = name and then we say
        # what fidos name is in the brackets of Dog() as well as his colour
        self.name = name
        self.colour = colour
        self.animal_kind = "Canine"


    def bark(self):  # self refers to the class
        return "woof"

# in order to execute a class we have to create an object of this class
fido = Dog("fido", "brown")  # Creating an object of our Dog class



print(fido)
print(fido.name) # fido is fido...
print(fido.colour) # Fido is brown
print(fido.animal_kind) # Fido is a canine
print(fido.bark()) # Fido barks woof
print("___________________")


print("Below are lassie's results objects ")
lassie = Dog("lassie", "cream") # Creating an object of our Dog class
print(lassie.name)
print(lassie.colour)
print(lassie.animal_kind)
print((lassie.bark()))


fido.animal_kind = "Big Dog"
# Changing the animal_kind for fido
# will not have any impact on the main Dog() class, so will not impact lassie
print("fido changed to Big Dog -----> " + fido.animal_kind)
print("lassie is unaffected -----> " + lassie.animal_kind)


