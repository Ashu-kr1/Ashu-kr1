class Bank:

    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount

    def check_balance(self):
        print(self.balance)

    def show_me_account_number(self,is_auth):
        if is_auth == True:
            print(self.account_number)
        else:
            print("Not allowed")

    def __internal_method(self):
        print("Private Method")
        print(self.__account_number)
        self.show_me_account_number()

hdfc = Bank(7707073263,1000)
hdfc.check_balance()
hdfc.deposit(1500)
hdfc.check_balance()
hdfc.show_me_account_number(True)



