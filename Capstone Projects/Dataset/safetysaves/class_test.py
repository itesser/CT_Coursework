from time import time


class Bacon:
    def __init__(self):
        self.life = 4
        self.blabber = "blach"
        bobo = "nada"
        self.this_at = time()


c = Bacon()

print(vars(c))
here = vars(c).keys()

print(here)
print(list(here))
