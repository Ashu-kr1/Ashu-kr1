## Conditional Loops

# Write a program to take a user age and let him know if he can go the club.
# 21

# Logic Building
# 1. user input - data type -> int
# o/p -> String -> user if he can go or not.


# 2. Rough loigc
# age  > 21 -> print can go
# age < 21 -> print can't go

club = int(input("Enter your age"))
if club >= 21:
    print(f"can go the club {club}")
else:
    print(f"can't go the club -> {club}")
