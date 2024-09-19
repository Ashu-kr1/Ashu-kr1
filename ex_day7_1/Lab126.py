#Multilevel Ineritance

class Grandfather:
    gold="2KG"
    def bhk1(self):
        print("1BHK")

class Father(Grandfather):
    diamond="22 Karat"

    def bhk2(self):
        print("2BHK")

class Son(Father):
    bitcoin="1BTC"

    def bhk3(self):
        print("3BHK")
s=Son
f=Father
gf=Grandfather

