"""
# number = 3.14159265359
# formated_number = f"{number:.2f}"
# print(formated_number)
#
#
# Format String
"""
num = 100
print("This is the number where i'm working with",num)
print("This is the number where i'm working with",f"{num}")

"""
Table
2 x 1 = 2 
2 x 2 = 4
2 x 3 = 6  
"""
table=9
print(f"{table}*1={table}")
print(f"{table}*2={table*2}")
print(f"{table}*3={table*3}")

# Home Can you create a Program I will give you number(userinput and print table)

Table_Number=int(input("enter the number for table output"))
for j in range(1,11):
    Table = f"{Table_Number}*{j} = {Table_Number * j}"
    print(Table)
