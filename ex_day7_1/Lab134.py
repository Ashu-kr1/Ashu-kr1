class GF:
    def car(self):
        return "old car"
class F(GF):
    pass
class S(F):
    pass
son=S()
print(son.car())