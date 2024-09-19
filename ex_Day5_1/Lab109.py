#Constructor
#Special Function in Class, __init__()
#It will be automically called when you create an object

class Dog:
    name = None # Instance Variable
    age = None

    def __init__(self,name,age):
        print("Called, Object is created")
        self.name = name
        self.age = age

    def sleep(self):
        local_variable=10
        print("Sleeping")
        print("Who is sleeping->",self.name,self.age)
        return None

dog1=Dog("Chow",19)
print(dog1.name)
dog1.sleep()
print(id(dog1))

dog2 = Dog("mow",20)
print(dog2.name)
dog2.sleep()
