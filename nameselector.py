#random person names from list selector
import random


#taking input from user
names = input("What is your friends names enter followed by comma and space\n").split(", ")

#calculating total names
total_person = len(names) - 1

#generating random index number
person = random.randint(0, total_person)

print(f"{names[person]} is going to buy the meal today!")
