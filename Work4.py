#from audioop import avg
from itertools import count
#from pprint import pprint

people = [
     ["Masha", "Kiev",35, True],
     ["Nic","Odessa",55, True],
     ["Mark","Dnipro",35, True],
     ["Mark","Kiev",18, False]
 ]
###############
all_married = []
not_married = []
city = "Kiev"
total_avg_age = 0

for person in people:
    is_married = person[3]
    address = person[1].lower()
    #address = address
    if is_married:
         #print(person, "married")
        all_married.append(person)
    if not is_married and city.lower() in address:
       not_married.append(person)

if all_married:
    for married_person in all_married:
        age = married_person[2]
        total_avg_age += age
    print(f"AVG age for married = {total_avg_age/len(all_married)}")


print("Married")
print(all_married)
print("Single")
print(not_married)


################
#all_married = []
#for person in people:
#    is_married = person[3]
#    if is_married:
         #print(person, "married")
#        all_married.append(person)
#    print(all_married)

#not_married = []
#city = "Kiev"
#for person in people:
#    is_married = person[3]
#    address= person[2].lower()
#    if not is_married and city.lower() in address:
#       not_married.append(person)
#    print(not_married)