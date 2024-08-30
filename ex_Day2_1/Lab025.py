#a = 10 # this is assignment -
#== -> true or false
a = 9 # int - whole numbrs -1, 2, 3
a=int(input("Enter the value"))
print(type(a))
if a==10:
    print(f"a  equal to if value")
else:
    print(f"a is not equal to if value")


# Problem to find the max between two

# Logic Building Formula

# 1 . user inputs -> two integers
# 2. o/ p ->  int 1 which ever is grater max number it will return.
# 3. - input method
# 31.4 or 45.34

num1=int(input("Enter the num1"))
num2=int(input("Enter the num2"))

if num1 > num2:
    print(f"Num1 is max{num1}")
else:
    print(f"Num2 is max{num2}")
