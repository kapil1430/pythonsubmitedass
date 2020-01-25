from deck import Pofdeck
class hand:
    def __init__(self):
        self.val=0
        self.list_of_cards=[]
        
    def draw_from(self,d):
        deck=d.return_cards()
        self.val+=deck[0].getval()
        self.list_of_cards.append(deck[0])
        #del d[0]
        return self.val

    def return_to(self):
        return self.list_of_cards
    
