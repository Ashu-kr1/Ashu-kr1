a = 20


class Person:
    b = 12  # Instanse - Belong to class
    c = 11  # Instanse - Belong to class

    def arint_infor(self):
        global a  # Declare it as global
        #a = "Hello"
        print(self.b)
        print(self.c)


object_ref = Person()
object_ref.arint_infor()
print(a)
