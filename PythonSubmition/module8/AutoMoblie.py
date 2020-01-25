class Automobile:
    def __init__(self,make,model,mileage,price):
        self.make=make
        self.model=model
        self.mileage=mileage
        self.price=price
        print('Its Constructor of Automobile')

    def get_make(self):
        return self.make
    def set_make(self,make):
        self.make=make
        
    def get_model(self):
        return self.model
    def set_model(self,make):
        self.model=model
        
    def get_mileage(self):
        return self.mileage
    def set_mileage(self,mileage):
        self.mileage=mileage

    def get_price(self):
        return self.price
    def set_price(self,price):
        self.price=price
