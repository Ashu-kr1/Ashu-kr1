# Functions scope
pb_global_b = 12 # almost work like a global varibale
def my_function():
    pb_local=21
    print(pb_local)
    print(pb_global_b)

my_function()
print(pb_global_b)

public_toilet = "PB"

# local variables have more preference as comapre to public variables



def home():
    private_toilet = "PT"
    print(private_toilet)
    public_toilet = "LPB"
    print(public_toilet)


home()


def strange():
    print(public_toilet)
    # print(private_toilet)


print(public_toilet)
# print(private_toilet)