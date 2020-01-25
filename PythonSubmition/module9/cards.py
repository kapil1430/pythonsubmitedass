class card:
    def __init__(self,suit,val):
        self.val=val
        self.suit=suit
        
    def __str__(self):
        return f'{self.suit} {self.val}'
    def get_val(self):
        return self.val
    


