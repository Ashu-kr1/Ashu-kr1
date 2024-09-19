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


object_ref = Calc()
a = float(input("Enter the value of a"))
b = float(input("Enter the value of b"))

sum = object_ref.sum(a, b)
sub = object_ref.sub(a, b)
mul = object_ref.mul(a, b)
div = object_ref.div(a, b)
print(sum, sub, mul, div)
