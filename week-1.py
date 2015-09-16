import random
gameStake = 50
cards = range(10)

class Player:
    InputID = 0
    startingPot = 0
    
    def __init__(self, inputID, StartingPot):
        self.InputID = inputID
        self.startingPot = StartingPot
        
    
    def play(self, dealerCard):
    
        playerCard = random.choice (cards)

        if playerCard < dealerCard:
            self.startingPot = self.startingPot - gameStake
            result = "Lose"
            return result + ', ' + str(playerCard)
        else:
            self.startingPot = self.startingPot + gameStake
            result = "Win"
            return result + ', ' + str(playerCard)

    def returnPot (self):
            return self.startingPot

    def returnID (self):
            return self.InputID


def playHand (players):
    for player in players:
        dealerCard = random.choice(cards)
        final = player.play(dealerCard)
        print "Player " + str(player.returnID()+1) + ' ' + final + ' vs ' + str(dealerCard)
        
        
        

def checkBalances (players):

    for player in players:
        print "Player " + str(player.returnID()+1) + " has " + "$" + str(player.startingPot) + " left"

players = []
for i in range(5):
    players.append(Player(i,500))

for i in range (10):
    print ''
    print 'Start game ' + str(i+1)
    playHand (players)

print ''
print 'Game results:'
checkBalances (players)

    
    

        
        
