from AutoMoblie import Automobile

class car(Automobile):
    def __init__(self,make,model,mileage,price,door):
        self.door=door
        Automobile.__init__(self,make,model,mileage,price)
    def get_door(self):
        return self.door
    def  set_door(self,door):
        self.door=door

class Truck(Automobile):
    def __init__(self,make,model,mileage,price,derive_type):
        self.derive_type=derive_type
        Automobile.__init__(self,make,model,mileage,price)

    def get_deriveType(self):
        return self.derive_type
    def  set_deriveType(self,derive_type):
        self.derive_type=derive_type

class suv(Automobile):
    def __init__(self,make,model,mileage,price,door,pass_cap):
        self.pass_cap=pass_cap
        Automobile.__init__(self,make,model,mileage,price)

    def get_passCap(self):
        return self.pass_cap
    def  set_passCap(self,pass_cap):
        self.pass_cap=pass_cap

co=car(2012,'Duster',22.45,1000000,'Auto')
print("---------------------YOUR CAR INFORMATION -------------------")
print(co.get_make())
print(co.get_model())
print(co.get_price())
print(co.get_mileage())
print(co.get_door())
To=Truck(2012,'Duster',22.45,1000000,'Autohandel')
print("---------------------YOUR TRUCK INFORMATION -------------------")
print(To.get_make())
print(To.get_model())
print(To.get_price())
print(To.get_mileage())
print(To.get_deriveType())

so=suv(2002,'TracK32',22.45,1000000,'Yes')
print("---------------------YOUR SUV INFORMATION -------------------")
print(so.get_make())
print(so.get_model())
print(so.get_price())
print(so.get_mileage())
print(so.get_passCap())


