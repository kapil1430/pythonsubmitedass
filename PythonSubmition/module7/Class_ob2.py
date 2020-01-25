class car:
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
    def __str__(self):
        return f'a {self.color} car'
o=car('red',70)
print(o.__str__())
