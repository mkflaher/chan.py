import random

countries = []
hobbies = []

with open('countries.txt') as cou:
    countries = cou.readlines()
with open('hobbies.txt') as hob:
    hobbies = hob.readlines()

countries = [c.strip('\n') for c in countries]
hobbies = [h.strip('\n') for h in hobbies]

string = "4chan is a " + random.choice(countries) + " " + random.choice(hobbies) + " forum."

print(string)
