#Polymorphism (message passing is agnostic to class)
# It's time to add our while loop back to our app so we can interact with our Pet instances.
# We'll build on the previous version of the loop by providing an option to adopt new Pet instances (including CuddlyPet). These are in pet.py.
# It's in this file where our while loop will go. In this file, we'll import our two classes so we can create new instances.

# Here's a skeleton version of our while loop, using a few helper functions to collect the user input and make sure the user has made a valid choice:

from pet import Pet, CuddlyPet
from toy import Toy

# Begin with no pets.
pets = []

main_menu = [   
    "Adopt a Pet",
    "Play with Pet",
    "Feed Pet",
    "View status of pets",
    "Give a toy to all your pets",
    "Do nothing",
]

def print_menu_error():
    print("That was not a valid choice. Try again.\n\n\n")    

def choices_to_string(choice_list):
    choice_string = ""
    num = 1
    for choice in choice_list:
        choice_string += "%d: %s\n" % (num, choice)
        num += 1
    choice_string += "Please choose an option: "
    return choice_string

def get_user_choice(choice_list):
    choice = -1
    choice_string = choices_to_string(choice_list)
    while choice == -1:
        try:
            choice = int(input(choice_string))
            if choice <= 0 or choice > len(choice_list):
                raise ValueError
        except ValueError:
            print_menu_error()
    return choice

#Add an adoption_menu variable to hold a list of pet choices. Then, prompt the user (in the main function below) to choose a type of pet to adopt. This will allow us to avoid checking between instances of Pet and CuddlyPet and not confuse the two. 

adoption_menu = [
    "Pet",
    "Cuddly Pet"
]


def main():    
    while True:
        choice = get_user_choice(main_menu)
        if choice == 1:
            pet_name = input("What would you like to name your pet? ")
            print("Please choose the type of pet: ")
            type_choice = get_user_choice(adoption_menu)
            if type_choice == 1:
                pets.append(Pet(pet_name))
            elif type_choice == 2:
                pets.append(CuddlyPet(pet_name))
            if len(pets) == 1:
                print("You now have 1 pet.")
            else: 
                print("You now have %d pets." % len(pets)) # Added this if-else to correct grammar
        if choice == 2:
            for pet in pets:
                pet.get_love()
        if choice == 3:
            for pet in pets:
                pet.eat_food()
        if choice == 4:
            for pet in pets:
                print(pet)
        if choice == 5:
            for pet in pets:
                pet.get_toy(Toy())
        if choice == 6:
            #Pet levels naturally lower.
            for pet in pets:
                pet.be_alive()
main()

# At this point, you should be able to adopt either a Pet or a CuddlyPet. When you choose 4 to "View status of pets", each pet should correctly use __str__() to print its status.
# In Object-Oriented Programming, this has a special name - polymorphism. What this means is that regardless of the class used to create an instance, as long as the class (or its superclass) defines a particular method, the instance can respond to that message.
# Put plainly, you don't have to know what kind of thing it is. You only have to pass it a message that it can respond to.

# Method resolution
# When you perform a function call, such as benji.get_love(), Python checks if that object knows how to get_love(). If the class benji belongs to didn't define that method, Python checks the superclass. If that class didn't define it, Python checks the superclass of the superclass.
# It does this until it finds the method or runs out of superclasses to check.

