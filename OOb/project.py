print("These are two dogs")

class Dog:
    species = "Golden Retriever"
    specie  = "Labrador Retriever"

    def __init__(self, name, age):
        self.name = name
        self.age = age


bud = Dog("Blu", "10–12 years")
dud = Dog("Woo", "10–12 years") 

print("Blu is a {}".format(bud.species))
print("But, Woo is a {}".format(dud.specie))

print("{} lives up to {} years old".format(bud.name, bud.age))
print("{} also lives up to {} years old".format(dud.name, dud.age))