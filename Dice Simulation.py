#TO GENERATE A RANDOM NUMBER Between 1 AND 6 (SIMULATES A DICE)
import random
print("U will get a number a between 1 and 6...")
def random_chance():
    ans='yes'
    while ans=='yes':
        x=random.randint(1,6)
        print("The number u have got is --> ",x)
        ans=input("U wanna continue (yes or no) :")       
random_chance()
