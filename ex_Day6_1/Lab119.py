class Car:
    def __init__(self,o_name,o_make,o_model):
        self.name=o_name
        self.make=o_make
        self.model=o_model
    def start_engine(self):
        print("Starting a car with name of " +self.name)
        print("Starting a car with make of " +self.make)
        print("Starting a car with model of " +self.model)
lambo = Car("lambo","V2","2024")

lambo.start_engine()

Nexon=Car("Nexon XMA","Automtic","2023")
Nexon.start_engine()