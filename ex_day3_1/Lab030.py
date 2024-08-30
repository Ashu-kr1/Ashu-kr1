# Pizza lover -yes

def make_pizza(*toppings):
    for topin in toppings:
        print(topin)

print("program stared")
ashu=make_pizza("Chicken")
print("program end")

# Built *
r = max(1, 2, 3, 4, 6)
print(r)

def make_pizaz(*topping,base):
    print(topping,base)
make_pizaz("mushroom", "tomato", "cheese", base="thin crust")
