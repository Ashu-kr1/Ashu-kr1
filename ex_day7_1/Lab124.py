## Inhertiance

class Father:
    key="2BHK"
    def car(self):
        print("Father Car !!","ALTO",self.key)

class Son(Father):
    key2="3BHK"

    def home(self):
        print("3BHK")
    def car2(self):
        print("XUV 700")

father_obj=Father()
#father_obj.car()

son_obj = Son()
son_obj.car()