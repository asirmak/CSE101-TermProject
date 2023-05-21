import random

class UnoCards:   # we will use this class to create card 

    def __init__ (self, colour, number):
        self.c = colour
        self.n = number

    def __str__ (self):  # string representation of card
        return "{} {}".format(self.c, str(self.n))

    def canPlay (self, other):      # We can compare the cards in each other
        if self.c == other.c or self.n == other.n:
            return True
        else:
            return False

class CollectionOfUnoCards:    # we will use this class to make deck 

    def __init__ (self):       # self.cards refers to deck
        self.cards = []
        self.thrownCards = []  # self.thrownCards refers to cards which are thrown by players

    def addCard (self, c):     # each card appends to deck
        self.cards.append(c)

    def makeDeck (self):       # deck is made 
        colours = ["Blue", "Red", "Yellow", "Green"]  
        for repeat in range (2):                     # we want 72 cards so, we have to multiply by 2
            for colour in colours:
                for num in range (1, 10):
                    card = UnoCards(colour, num)
                    self.addCard(card)
        self.shuffle()

    def shuffle (self):        # deck is shuffled
        for q in range (len(self.cards)):
            random_element = random.randint(0, 71)
            self.cards[q], self.cards[random_element] = self.cards[random_element], self.cards[q]

    def getTopCard(self):     # it allows us to get last thrown card
        return self.thrownCards[-1]

    def canPlay(self,other):  # it allows us to compare cards whether they are playable in each other or not by the help of "UnoCards class canPlay function"
        lastPlayedCard = self.getTopCard()
        if UnoCards.canPlay(lastPlayedCard, other):
            return True
        else:
            return False

    def __str__ (self):     # string representation of deck
        stringDeck = ""
        for var1 in self.cards:
            stringDeck += str(var1) + ", "
        return stringDeck

class Uno:
    def __init__(self):
        self.deck = CollectionOfUnoCards() 
        self.deck.makeDeck()    # we call "makeDeck" function in "CollectionOfUnoCards" class to make deck
        self.hand1 = []   # self.hand1 refers to player 1's cards
        self.hand2 = []   # self.hand2 refers to player 2's cards
        for i in range (7):  # players' cards are dealt one by one
            ourDeck = self.deck.cards[i]
            self.hand1.append(ourDeck)
            self.deck.cards.pop(i)
            ourDeck = self.deck.cards[i]
            self.hand2.append(ourDeck)

    def printResult(self, player):   # this function prints result
        if player == "player1":
            print("Player 1 is winner")
        elif player == "player2":
            print("Player 2 is winner")
        else:
            print("Nobody won the game")

    def playGame(self): # First round is played by a randomly selected player. After that, game is played in order
        player_list = ["player1", "player2"]     # Player 1 is human, Player 2 is python
        player1or2 = random.choice(player_list)     
        if player1or2 == "player1":                 
            print("Player 1 started the game")               
            stringHand1_ = ""
            for q in self.hand1:
                stringHand1_ += str(q) + ", "
            print("Player 1's cards are" , stringHand1_)
            A = True
            while A == True:
                indexOfCard = int(input("Which card do you want to play. You can play between 1 to " + str(len(self.hand1)) + " ? "))
                if indexOfCard > len(self.hand1) or indexOfCard <= 0:
                    print("Please enter a playable card from your hand")
                    A = True
                else:
                    A = False
                    chooseCard = self.hand1[indexOfCard-1]            
                    self.deck.thrownCards.append(chooseCard)
                    self.hand1.remove(chooseCard)
                    print("Player 1 played", chooseCard, "-- Player 2's turn" + "\n" + len(self.deck.cards)*"-")
                    self.playTurn("player2")
        else:                                       
            print("Player 2 started the game")                   
            string2 = ""
            for zxd in self.hand2:
                string2 += str(zxd) + ", "
            print("Player 2's cards are" , string2)
            random_card2 = random.choice(self.hand2)
            self.deck.thrownCards.append(random_card2)
            self.hand2.remove(random_card2)
            print("Player 2 played", random_card2, "-- Player 1's turn" + "\n" + len(self.deck.cards)*"-")
            self.playTurn("player1")

    def playTurn(self, player): 
        if player == "player1":
            stringHand1 = ""
            for j in self.hand1:
                stringHand1 += str(j) + ", "  # string representation of player 1's cards
            stringHand2 = ""
            for k in self.hand2:
                stringHand2 += str(k) + ", "  # string representation of player 2's cards
            print("Player 1's cards are", stringHand1 + "\n" + "Player 2's cards are", stringHand2 + "\n" + "CARDS IN DECK\n" + str(self.deck) + "\n" + len(self.deck.cards)//2*"/")
            
            playableCards = []          # playable cards are determined
            NonPlayableCards = []       # nonPlayable cards are determined 
            for card1 in self.hand1:
                if self.deck.canPlay(card1):
                    playableCards.append(card1)
                else:
                    NonPlayableCards.append(card1)
            
            playableCardsString = ""
            for eachPlayableCard in playableCards:
                playableCardsString += str(eachPlayableCard) + ", " # string representation of playable cards

            if len(self.deck.cards) == 0:   # if there is no cards in deck, game will finish
                print("No cards in the deck")
                self.printResult("Nobody")

            elif len(self.hand1) == 0:       # if player 1 does not have any cards, game will finish
                print("Player 1 does not have any cards")
                self.printResult(player)
            
            else:
                if len(NonPlayableCards) == len(self.hand1):  # if player 1's whole cards are not playable that means there is not playable cards
                    print("Last played card is", self.deck.getTopCard(), "\nThere is no playable card. Draw a card!")
                    self.hand1.append(self.deck.cards.pop(0))
                    print("Player 1 has drawn a card. -- Player 2's turn" + "\n" + len(self.deck.cards)*"-")
                    self.playTurn("player2")

                else:
                    print("Last played card is", self.deck.getTopCard())
                    print("Player 1 can play", playableCardsString + "against", self.deck.getTopCard())
                    A = True
                    while A == True:
                        indexOfCard = int(input("Which card do you want to play. You can play between 1 to " + str(len(self.hand1)) + " ? "))
                        if indexOfCard > len(self.hand1) or indexOfCard <= 0:
                            print("Please enter a playable card from your hand")
                            A = True
                        else:
                            if self.hand1[indexOfCard-1] in NonPlayableCards:
                                print("Please enter a playable card from your hand")
                                A = True
                            elif self.hand1[indexOfCard-1] in playableCards:
                                A = False
                                chooseCard = self.hand1[indexOfCard-1]
                                self.deck.thrownCards.append(chooseCard)
                                self.hand1.remove(chooseCard)
                                print("Player 1 played", chooseCard, "-- Player 2's turn" + "\n" + len(self.deck.cards)*"-")
                                self.playTurn("player2")

        elif player == "player2":
            stringHand1 = ""
            for j in self.hand1:
                stringHand1 += str(j) + ", " # string representation of player 1's cards
            
            stringHand2 = ""
            for k in self.hand2:
                stringHand2 += str(k) + ", "    # string representation of player 2's cards
            
            print("Player 1's cards are", stringHand1 + "\n" + "Player 2's cards are", stringHand2 + "\n" + "CARDS IN DECK\n" + str(self.deck) + "\n" + len(self.deck.cards)//2*"/")
            
            playableCards2 = []     # playable cards are determined 
            NonPlayableCards2 = []      # nonPlayable cards are determined 
            for card2 in self.hand2:
                if self.deck.canPlay(card2):
                    playableCards2.append(card2)
                else:
                    NonPlayableCards2.append(card2)
            playableCards2String = ""
            for eachPlayableCard2 in playableCards2:
                playableCards2String += str(eachPlayableCard2) + ", "  # string representation of playable cards
            
            if len(self.deck.cards) == 0:   # if there is no cards in deck, game will finish
                print("No cards in the deck")
                self.printResult("Nobody")

            elif len(self.hand2) == 0:      # if player 2 does not have any cards, game will finish
                print("Player 2 does not have any cards")
                self.printResult(player)

            else:
                if len(NonPlayableCards2) == len(self.hand2):       # if player 2's whole cards are not playable that means there is not playable cards
                    print("Last played card is", self.deck.getTopCard(), "\nThere is no playable card. Draw a card!")
                    self.hand2.append(self.deck.cards.pop(0))
                    print("Player 2 has drawn a card. -- Player 1's turn" + "\n" + len(self.deck.cards)*"-")
                    self.playTurn("player1")
                else:
                    print("Last played card is", self.deck.getTopCard())
                    print("Player 2 can play", playableCards2String + "against", self.deck.getTopCard())
                    CardThatWillBePlayed = random.choice(playableCards2)
                    self.hand2.remove(CardThatWillBePlayed)
                    self.deck.thrownCards.append(CardThatWillBePlayed)
                    print("Player 2 played", str(CardThatWillBePlayed), "-- Player 1's turn" + "\n" + len(self.deck.cards)*"-")
                    self.playTurn("player1")

def main():
    my_game = Uno()
    my_game.playGame()

main()