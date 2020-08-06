class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5): #Self is customary and used by all devs
        self.name = name
        self.fullness = fullness
        self.happiness = happiness #We never have to call __init__ directly - Python automatically calls it when we make a new instance
        self.hunger = hunger
        self.mopiness = mopiness


#We now have a class that we can use to create instances with their own attribute values. But the real power of classes is the ability to define custom methods that make use of those attributes.
# We can add the methods eat_food() and get_love() for the Pet class. Each modifies the instance's attributes accordingly:

# Inheritance
# Another technique from Object-Oriented Programming involves making specialized versions of classes While an instance of the Pet class can be manually configured to be happy, creating many of them with the same constructor arguments is a sign that we need another class. This new class should be exactly like the Pet class, except with specific traits built into it. We'll tackle that in two parts. First, we'll make a subclass of Pet, taking on all of its properties and methods. Then we will handle the customizations.
# Here is how to make a subclass of Pet:

class CuddlyPet(Pet): #<--- because we want to make a different TYPE of pet
    def __init__(self, name, fullness=50, hunger=5):
        super().__init__(name, fullness, 100, hunger, 1) #With this technique, CuddlyPet could accept additional constructor arguments:
        self.cuddle_level = cuddle_level
        # self.name = name
        # self.fullness = fullness
        # self.happiness = 100
        # self.hunger = hunger
        # self.mopiness = 1 #Because we hard coded happiness and mopiness values, we can remove them from the parameter list. But it would be better to call Pet's __init__() from CuddlyPet's __init__. We will do that with a super(), and note out the attribute values
    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness/2 #<--- We added this function to OVERRIDE existing methods in the subclass, simply by redefining the method within the subclass. This OVERRIDES the be_alive() in the Pet class. An instance of CuddlyPet now stays happy for twice as long as the typical Pet. We will also override the __init__ method above by setting default values for self.happiness and self.mopiness
    def cuddle(self, other_pet):
        for i in range(self.cuddle_level)
            other_pet.get_love() #This method accepts the implicit argument self, and also accepts the argument other_pet - the target of the cuddle.
    #By putting Pet in parentheses next to the name of the class, we're telling Python that the CuddlyPet class inherits from Pet. A class that inherits from another is a SUBCLASS. SUBCLASSES inherit from SUPERCLASSES. They are simply classes that provide default attributes and methods for their subclasses.
    #Until adding new attributes to the subclass, it inherits all the same attributes from the superclass. 
    #We added new methods to the subclass with a new function called cuddle()
    #See below for the cuddle() method in action

# When should I add attributes to the superclass and when should I add them to subclasses?
# When you want to make a change to the superclass and all its subclasses, make the change to the superclass. If you only want the change to affect a specific subclass, only change that subclass.
# This works both for attributes as well as methods

    def eat_food(self):
        self.fullness += 30
    def get_love(self):
        self.happiness += 30

    #As with __init__, the first parameter is self, which is how the body of the method access the instance.
    #Each instance has its own eat_food() and get_love() methods. Calling cujo.eat_food() only affects the value of cujo.fullness. Likewise, calling benji.get_love() only affects the value of benji.happiness

    # Encapsulation
    # In Object-Oriented Programming, one of the main features of classes is that they provide a way to bundle state (attributes) and behavior (methods). This is known as encapsulation. Practicing good encapsulation is a matter of deciding the minimum amount of information an object needs to store in its state in order to do its work via its behaviors. Likewise, methods should have as few responsibilities as possible. As with functions, a method should have one clear and specific purpose.
    # Here, implementing be_alive() so that it decrements a certain amount of fullness and happiness:

    def be_alive(self, hunger, mopiness): #< -- Specializing be_alive with its own parameters of hunger and mopiness
        self.fullness -= hunger 
        self.happiness -= mopiness #This moves those to the constructor, but are not configurable (see initial def __init__).



# cujo = Pet("Cujo") # <--- We only need to provide NAME because fullness and happiness each have default values in the init function
# cujo.eat_food
# print(cujo.fullness)
# # 80
# print(cujo.happiness)
# # 50

# benji = Pet("Benji") #These create INSTANCES of the CLASS 'Pet'
# #You can call a class multiple times and get a different instance of the class. Some devs think of classes as 'factories' for new instances.
# #An individual object created from a class is known as an instance of that class. The function that creates instances is the CONSTRUCTOR, which here is the function underneath the initial class Pet.
# benji.get_love()
# print(cujo.fullness)
# #50
# print(benji.happiness)
# #80

benji = CuddlyPet("Benji", 50, 20, 20, 1)
cujo = Pet("Cujo", 50, 10, 30, 10)
print(cujo.happiness)
# 10
benji.cuddle(cujo)
print(cujo.happiness)
# 40
