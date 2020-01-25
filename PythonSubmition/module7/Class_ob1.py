import random
class coin:
    def __init__(self):
        self.sideup="'Heads'"
    def toss(self):
        if random.randint(0,1)==1:
            self.sideup='Heads'
        else:
            self.sideup='Tails'
    def gsideup(self):
        return self.sideup
o=coin()
print("BEFORE TOSS",o.gsideup())
o.toss()
print("AFFTER TOSS",o.gsideup())
