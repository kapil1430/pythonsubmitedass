class Information:
    def __init__(self,name,email,phone,address):
        self.name=name
        self.email=email
        self.phone=phone
        self.address=address
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name=name
    def get_Email(self):
        return self.email
    def set_Email(self,email):
        self.email=email
    def get_Phone(self):
        return self.phone
    def set_Phone(self,phone):
        self.phone=phone
    def get_Address(self):
        return self.address
    def set_Address(self,address):
        self.address=address
    def __str__(self):
        return f'Name Is {self.name} Email {self.email} your Phone {self.phone} and ADDRESS {self.address} Information'
def main():
    #it Fixes the values into init() constructor when we want to change in future we get change Though the setMethod()
    p1=Information("Kapil",'kplshrm1430@gmail.com','7389370811','Village Makodiya Indore Madhya Pradesh')
    p1.set_name('Kapil Sharma')
##    p1.set_Email('kplshrm1430@gmail.com')
##    p1.set_Phone('7389370811')
##    p1.set_Address('Village Makodiya Indore Madhya Pradesh')
    print("YOUR CONTACT INFORATION"+"\n"+p1.__str__())
main()   
