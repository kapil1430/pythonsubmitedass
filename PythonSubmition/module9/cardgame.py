import random
class card:
    def __init__(self,suit,val):
        self.val=val
        self.suit=suit
        
    def __str__(self):
        return f'{self.suit} {self.val}'
    
    def getval(self):
        return self.val

class deck:
    def __init__(self,ls):
        self.ls=ls
        
    def shuffle(self):
        self.ls=random.sample(self.ls,len(self.ls))

    def return_cards(self):
        return self.ls
    
def initilize():   
    ls=[]
    for i in range (1,14):
        c=card("hearts",i)
        ls.append(c)
    for i in range (1,14):
        c=card("diamond",i)
        ls.append(c) 
    for i in range (1,14):
        c=card("spade",i)
        ls.append(c)  
    for i in range (1,14):
        c=card("club",i)
        ls.append(c) 
    return ls

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
        
        
def play():
    d=deck(initilize())
    h=hand()
    while(True):
        d.shuffle()
        if(h.draw_from(d)>17):
            print("you won")
            break
        else:print("drawing a card")  
    
    
play()
            
        
        
        
        
        
        
        
        
        
        
        
        
        
