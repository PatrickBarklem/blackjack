'''
Time for blackjack and hookers*
                                                         *without the hookers
'''

from random import shuffle

class game:
    def __init__(self, numPlayers):
        self.nP = numPlayers
        self.gameDeck = deck()
        self.gameDeck.createNewDeck()

    def startRound(self):
        self.groupPlayers = []
        for i in range(self.nP):
            newPlayer = player(i)
            self.groupPlayers.append(newPlayer)
        for x in range(self.nP):
            for y in range(2):
                self.groupPlayers[x].receiveCard(self.gameDeck.dealCard())
            
class deck:
    def __init__(self):
        self.suit = ["Clubs","Diamonds","Hearts","Spades"]
        self.card = []
        self.deckContents = []

    def createNewDeck(self):
        #Creates a new deck and shuffles it
        self.deck = []
        for i in range(4):
            for x in range(1,14):
                self.card = [self.suit[i],x]
                self.deckContents.append(self.card)
        shuffle(self.deckContents)

    def printDeck(self):
        #prints deck for testing
        print (self.deckContents)

    def dealCard(self):
        #removes card from deck and returns value
        return self.deckContents.pop()
    
class player:
    def __init__(self,number):
        self.hand = []
        self.name = "Player: "+str((number+1))

    def printName(self):
        #test to see if object naming works
        print (self.name)

    def receiveCard(self,card):
        #add next card in deck to hand contents
        self.hand.append(card)
        print(self.name+str(self.hand)) #testing
        
if __name__ == "__main__":
    test = game(4)
    test.startRound()
    
    
