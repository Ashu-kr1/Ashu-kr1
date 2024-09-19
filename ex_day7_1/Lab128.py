# Multiple Inhertiance
class Father:
    key = "ABC"
    __password="private"

    def __show_password(self):
        print(self.__password)
    def father_money(self):
        return 5
    def home(self):
        return "This is from the Father Home"
    def show_everthing(self):
        self.__show_password()

class Mother:
    def mother_money(self):
        return 2

    def home(self):
        return "this is from the mother"

class Son(Mother,Father):
    pass
class Son2(Father,Mother):
    pass

obhect_son=Son()
print(obhect_son.father_money())
print(obhect_son.mother_money())
print(obhect_son.show_everthing())
print(obhect_son.mother_money())
print(obhect_son.home())
