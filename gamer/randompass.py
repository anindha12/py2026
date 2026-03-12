import random
import string

print("Welcome, This is the random Password generator!")
print("May I ask you for your name?")
name = input() 

print("What is the length of the password you want? Choose between 8 and 20 characters.")
length = int(input())


length = max(8, min(20, length))


characters = string.ascii_letters + string.digits
random_string = ''.join(random.choice(characters) for _ in range(length))

print("{} This is the Random Password you asked for: {}".format(name, random_string))   