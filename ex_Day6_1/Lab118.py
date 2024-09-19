class Person:
    # Class variabes
    # Instance variabes
    def __init__(self,name):
        self.name=name

    def walk(self):
        return self.name

ashu = Person("ashu")
pramod=Person("Pramod")
print(ashu.name)
print(pramod.name)
print(f"Who is walking with object{ashu.walk()}")