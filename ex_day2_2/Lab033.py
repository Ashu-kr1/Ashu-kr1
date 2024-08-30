# Match Statement
# match variable:
#     case pattern1:
#         # code block
#     case pattern2:
#         # code block

# Write a program to ask the user which browser he want to run automation

browser_name = input("Enter the name of browser")

match browser_name:
    case "firefox":
        print("Excute the firefox Code")
    case "chrome":
        print("Excute the chrome Code")
    case "edge":
        print("Excute the edge Code")
    case _:
        print("Browser not found")

user_type = input("Enter the user type, admin, manager, guest")
user_type=user_type.lower()
match user_type:
    case "admin" | "manager":
        print("Helo Sir")
    case "guest":
        print("Hi How i can help you")
    case _:
        print("Hello")
