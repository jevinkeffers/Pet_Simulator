# Composition (not everything should be a subclass)
# It's getting pretty tough to play with all these pups! You might consider getting some toys for them, each of which can provide them with a certain amount of happiness.

#When should I store additional information in another class?
# We might think that a toy might just be a Boolean field - does the pet have a toy or not? But what an individual Pet could have multiple toys? And what if each toy could provide a certain amount of happiness, or a limited lifespan?

# Once we start adding attributes to an attribute, it might be a good time to make another class.

class Toy:
    def __init__(self, bonus=10, newness=10):
        self.bonus = 10
        self.newness = 10
# And finally, we need to define what it means for a Toy to be played with. Each time we use() a Toy, it should decrease in newness and it should return a happiness bonus.
    def use(self):
        if self.newness == 0:
            return 0
        else:
            self.newness -= 1
            return self.bonus
