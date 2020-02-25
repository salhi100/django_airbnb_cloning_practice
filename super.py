# father class
class Dog:
    # inside is method
    # outside is function
    def __init__(self):
        print("woof")

    def pee(self):
        print("I will pee")


# child class of Dog
class Puppy(Dog):
    def pee(self):
        print("go to the park")

        # super allows you to access methods in father class
        super().__init__()
        super().pee()


pug = Puppy()

pug.pee()
