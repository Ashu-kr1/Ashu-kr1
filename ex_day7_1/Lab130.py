class Grandparent:
    key_world = "1kg"

    def gransparent_method(self):
        return "Grandparent's method"


class Parent(Grandparent):
    def parent_method(self):
        return "Parent"


class Child(Parent):
    mac_m3_apple = "M3 MAX"

    def child_method(self):
        return "Child's method"
child=Child()
print(child.gransparent_method())