# ● Take a input from a user and print the table

Input_Number = int(input("Enter any number which you want see the table"))
for i in range(1,11):
    table= f"{Input_Number}*{i} = {Input_Number * i } "
    print(table)