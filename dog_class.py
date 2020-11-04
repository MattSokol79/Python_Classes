# Classes, objects and instantciation

# How to create class
# Synatx: class name_of_class starting with Capital letter
# good naming convention is required

# classes are a way to bring data and functionality together
class Dog:

    animal_kind = "Canine is running"   # defining class variable

    def bark(self):  # self refers to current class
        return "woof"

# in order to execute a class we have to create an object of this class
fido = Dog()  # Creating an object of our Dog class

print(fido)
print(fido.animal_kind) # Fido is a canine
print(fido.bark()) # Fido barks woof

print("Below are lassie's results objects ")
lassie = Dog() # Creating an object of our Dog class
print((lassie.bark()))
print(lassie.animal_kind)

fido.animal_kind = "Big Dog"
# Changing the animal_kind for fido
# will not have any impact on the main Dog() class, so will not impact lassie
print("fido changed to Big Dog -----> " + fido.animal_kind)
print("lassie is unaffected -----> " + lassie.animal_kind)


