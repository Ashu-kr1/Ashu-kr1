a = 10
class Myclass:

    #public var(instance)
    public_var = "I am Public"
    __balance = 100

    #Private variables
    __private_var = "I am private."
    __password = "1234"

    #Protected variable.
    _protected_var = "I am protected"
    b = 10
    _c = 20
    __d = 45
    college = "ABC"
    pramod = "TTA"
    __pramod_bank = 10000000

object = Myclass()
print(object.public_var)
print(object._protected_var)
#print(object.balance)
print(object.__private_var)
print(object.__password)
