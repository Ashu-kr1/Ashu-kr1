# Take input and create a class in python
class Person:
    def __init__(self):
        self.name=input("Enter your name\n")
        self.age=input("Enter your age\n")
        self.Phone=input("Enter your Phone\n")
        self.occupation=input("Enter your occupation\n")
    def name_of_the_function_to_display(self):
        print(f"Name is {self.name}",f"Age is {self.age}",f"Phone is {self.Phone}",f"Occupation is {self.occupation}")

#Create an object
Person1=Person()

#Call the display function
Person1.name_of_the_function_to_display()
