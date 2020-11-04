# Create a Cat class

# one function that returns "MEOWWWW"

# Create 2 class level variable
# Create 3 objects
# Display all information with each object
# Change the class variable values in each object and display
# Pseudo code each block of code

class Cat:

    animal_kind = "feline"

    tendency = "cuddly"

    def meow(Self):
        return "MEOWWWW"

# Creating 3 objects i.e. cats
ginger = Cat()
max = Cat()
frankie = Cat()

# Changing the variables for each object and then displaying the changes
# for every cat
ginger.animal_kind = "BIG feline"
ginger.tendency = "a little wuss"

print(f"ginger is a -----> " + ginger.animal_kind)
print(f"ginger has a tendency to be ------> " + ginger.tendency)
print(ginger.meow())


max.animal_kind = "small feline"
max.tendency = "scratch scratch"

print(f"max is a -----> " + max.animal_kind)
print(f"max has a tendency to ------> " + max.tendency)
print(max.meow())

frankie.animal_kind = "wild feline"
frankie.tendency = "a bit wild"

print(f"frankie is a -----> " + frankie.animal_kind)
print(f"frankie has a tendency to be ------> " + frankie.tendency)
print(frankie.meow())