import math

def give_me_power(num):
    return math.pow(num,2)

op=give_me_power(5)
print(op)

op2=lambda :math.pow(int(input("Enter the number")),2)
print(op2())