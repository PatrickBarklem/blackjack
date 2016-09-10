'''
Time for blackjack and hookers*
                                                         *without the hookers
'''

from random import shuffle

class game:
    def __init__(self, noPlayers):
        self.nP = noPlayers #decide how many players will be playing

class deck:
    def __init__(self):
        self.suit = ["Clubs","Diamonds","Hearts","Spades"]
        self.card = []
        self.deck = []

    def createDeck(self):
        #Creates a basic deck and shuffles it
        for i in range(4):
            for x in range(1,14):
                self.card = [self.suit[i],x]
                self.deck.append(self.card)
        shuffle(self.deck)
        

    def dealHand(self):
        return none

'''class player:
    return none '''
    
