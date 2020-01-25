import random
#from cards import card
class  Pofdeck:    
    def __init__(self,listOFcard):
        self.listOFcard=listOFcard

    #This method is return the shuffle list  
    def get_ShuffleCard(self):
        CardList=[]
        CardList=self.listOFcard
        self.listOFcard=random.sample(CardList,len(CardList))
##        for i in range(0,52):print(self.listOFcard[i].__str__())
        
    #This Method is used for 1 shuffled card return
    def Next_card(self):
        crdlist=[]
        crdlist=self.listOFcard
        HandCard_1=crdlist[0]
        return HandCard_1

    def Return_cardList(self):
        cardList=[]
        cardList=self.listOFcard
        return cardList
class card:
    def __init__(self,suit,val):
        self.val=val
        self.suit=suit
        
    def __str__(self):
        return f'{self.suit} {self.val}'
    def get_val(self):
        return self.val
    
def ListOfCard():
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
        self.listOfCard=[]
    def Draw_from(self,DeckList):
        self.val=DeckList[0].get_val()
        self.lisofCard.append(DeckList[0])
        
        
        
class Game:
    do=PofDeck(ListOfCard())
    h=hand()
