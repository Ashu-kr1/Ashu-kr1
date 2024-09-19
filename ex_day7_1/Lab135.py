class Calc:

    def __init__(self):
        print("DC")

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


obj_ref = Calc()

a = int(input("Enter the value a"))
b = int(input("Enter the value b"))

print(obj_ref.sum(a,b))
