import random
print("This is a Command user interface Dice Rolling Simultor")
max=6
min=1
raw_input='y'
while raw_input=='yes' or raw_input=='y':
    print("Dices are Rolling/n")
    print("the Values Are:/n")
    print (random.randint(min,max))
    print (random.randint(min,max))
    raw_input=input("Want To Roll Again")
print("Thank You For using Our Services")