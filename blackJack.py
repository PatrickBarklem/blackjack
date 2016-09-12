'''
Time for blackjack and hookers*
                                                         *without the hookers
'''

import random

class game:
    def __init__(self, numPlayers):
        self.nP = numPlayers
        self.gameDeck = deck()
        self.gameDeck.createNewDeck()

    def startRound(self):
        self.groupPlayers = []
        self.dealer = player(True,False,0)
        for i in range(self.nP):
            if i == 0:
                newPlayer = player(False,True,i)
            else:
                newPlayer = player(False,False,i)
            self.groupPlayers.append(newPlayer)
        #deal dealer cards
        for x in range(2):
            self.dealer.receiveCard(self.gameDeck.dealCard())
        #deal players cards
        for o in range(self.nP):
            for y in range(2):
                self.groupPlayers[o].receiveCard(self.gameDeck.dealCard())
            self.groupPlayers[o].calculateHandValue()
        
    def betting(self):
        #calls bet function from all players in player group
        for i in range(self.nP):
            self.groupPlayers[i].placeBet()
    

        
class deck:
    def __init__(self):
        self.suit = ["Clubs","Diamonds","Hearts","Spades"]
        self.card = []
        self.deckContents = []

    def createNewDeck(self):
        #Creates a new deck and shuffles it
        self.deck = []
        for i in range(len(self.suit)):
            for x in range(1,14):
                self.card = [self.suit[i],x]
                self.deckContents.append(self.card)
        random.shuffle(self.deckContents)

    def printDeck(self):
        #prints deck for testing
        print (self.deckContents)

    def dealCard(self):
        #removes card from deck and returns value
        return self.deckContents.pop()
    
class player:
    def __init__(self,dealer,human,identity):
        self.human = human
        self.hand = []
        self.bust = False
        self.money = 100
        self.betValue = 0
        self.handValue = 0
        if dealer == False:
            self.name = "Player "+str((identity+1))
        else:
            self.name = "Dealer"

    def printName(self):
        #test to see if object naming works
        print (self.name)

    def receiveCard(self,card):
        #add next card in deck to hand contents
        '''
        print(card)
        if card[1] == 1:
            card[1] = "Ace"
        elif card[1] == 11:
            card[1] = "Jack"
        elif card[1] == 12:
            card[1] = "Queen"
        elif card[1] == 13:
            card[1] = "King"
        '''
        self.hand.append(card)
        #print(self.name,str(self.hand)) testing dealing and changing values to str if picture card or ace

    def placeBet(self):
        #set bet amount, checks if it's the human player
        if self.human == True:
            print("Current Money: ",self.money)
            self.betValue = input("Enter amount to bet: ")
            self.money -= int(self.betValue)
        else:
            self.betValue = random.randint(1,int(self.money*0.75))
            self.money -= int(self.betValue)
        print(self.name," has bet ",self.betValue)

    def calculateHandValue(self):
        for i in range(len(self.hand)):
            if self.hand[i][1] == 11 or self.hand[i][1] == 12 or self.hand[i][1] == 13:
                self.handValue += 10
            else:
                self.handValue += self.hand[i][1]
        '''    print("Card ",i+1," is ",self.hand[i][1]) checking 
        print (self.handValue)
        '''
        #testing if value changing works for picture cards
            
        
if __name__ == "__main__":
    test = game(4)
    test.startRound()
    test.betting()
    
    
