def sum_three_num(a,b,c):
    return a,b,c

ol=lambda a,b,c:a+b+c
print(ol(5,8,9))

def find_odd_even(num):
    if num % 2 ==0:
        print("Even")
    else:
        print("Odd")

print(find_odd_even(5))

# find the odd_even_number

check_odd_even=lambda num : "Even" if num%2==0 else "Odd"
print(check_odd_even(12))