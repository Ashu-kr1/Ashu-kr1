class Dog:# Class Name will always start from capital letter
    #A
    name = None
    breed = None
    Color = None
    #B
    def sleep(self):
        print("Sleeping")
    def bark(self):
        print("bark")
    def eat(self,food):
        print(food)

dog1=Dog()
print(dog1.name)
dog1.name = "Chow"
print(dog1.name)
dog1.sleep()

print(" ---- -----------------")

dog2=Dog()
dog2.name="Mow"
print(dog2.name)
dog2.eat("meat")