class Dog(object):
    #
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        self.li = [1,3,4]
        
    def speak(self):
        print("Hi I am", self.name, "and I am", self.age)

    def change_age(self,age):
        self.age = age

    def add_weight(self, weight):
        self.weight = weight

tim = Dog('Tim', 21)
fred = Dog('Fred', 23)
tim.change_age(5)
tim.add_weight(70)
tim.speak()
fred.speak()

print(fred.weight)

