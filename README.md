# Day 3 - Classes
## OOP - Object Oriented Programming
### There are 4 pillars
1. Inheritance (most used) - **Eliminates redundant code**.
We can use all functions and variable from parent class
2. Encapsulation - **Reduce complexity and increase reusability**.
Also used to reduce access, making private methods/
variables etc.
3. Abstraction - **Reduce complexity and isolate impact of changes**.

4. Polymorphism (Many Forms) - **Refactor code or case statements**.
It allows us to change behaviour or attributes
/ variables 

**What are classes?:**
- Class is the main factor that is 
used to implement any of these 
pillars

### Creating a class
```python
class Class_name:
    variable = "Something"

    def function(self):
        return "Something"
```

### Dog Class Example
As an introduction to coding classes, we 
created a simple Dog class:

[Dog](https://github.com/MattSokol79/Python_Classes/blob/main/dog_class.py)

```python
# Classes, objects and instantiating

# How to create class
# Synatx: class name_of_class starting with Capital letter
# good naming convention is required

# classes are a way to bring data and functionality together
class Dog:

    animal_kind = "Canine is running"   # defining class variable

    def bark(self):  # self refers to fido. in this case
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

```
### Task - Cat Class
Practiced the concepts by
creating a basic Cat class.

[Cat](https://github.com/MattSokol79/Python_Classes/blob/main/cat_class.py)

