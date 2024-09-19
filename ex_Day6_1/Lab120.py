# Web Automation - Selenium
# Page - You are going automate

class VWOLoginPage:
    def __init__(self,email_arg,password_arg):
        self.email=email_arg
        self.password=password_arg

    def Login_confirm(self):
        if self.email=="ashur854@gmail.com" and self.password=="Pass143":
            print("Allowed to Login")
        else:
            print("not allowed to login")
 # This is the end of the class

email=input("Enter the email\n")
password=input("Enter the password\n")
vwo_object=VWOLoginPage(email,password)
vwo_object.Login_confirm()