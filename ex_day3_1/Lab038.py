# Create a program to sum of three number from the user input

num1 = int(input("Enter the the number 1")) # 100
num2 = int(input("Enter the the number 2")) # 200
num3 = int(input("Enter the the number 3")) # 300

def sum_of_3_number(n1,n2,n3):
    return n1+n2+n3

result=sum_of_3_number(num1,num2,num3)
print(result)

def sum_of_two_number(a, b):
    return a + b

result_sum1 = sum_of_two_number(10, 30)
result_sum2 = sum_of_two_number(20, 50)
print(result_sum1)
print(result_sum2)

def sum_of_three_number(a=5, b=10, c=15):
    return a + b + c


# result = sum_of_three_number(10, 20, 30)
# result = sum_of_three_number(10, 20)
# result = sum_of_three_number(10)
# result = sum_of_three_number()
result = sum_of_three_number(a=78, c=67)
print(result)

def sum_three(a=1, b=1, c=1):
    return a + b + c


# result1 = sum_three()
# print(result1)

# result2 = sum_three(1, 2)
# print(result2)

# result3 = sum_three(1, 2, 3)
# print(result3)

# result5 = sum_three(b=67, a=10, c=45)
# print(result5)

# result4 = sum_three(a=10, b=67, c=45)
# print(result4)

# result6 = sum_three(a=10, b=67, c=45, 34)
# print(result6)