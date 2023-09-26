from points import Points
from card import Cards


class Director:
    """The Director class is responsable for control the sequence of play. Attributes: TODO add atributes."""

    def __init__(self):
        self.is_playing = True
        self.score = 0
        self.total_score = 300

    def start_game(self):
        self.card = Cards()
        while self.is_playing:
            self.getAnswer()
            self.compareValues()
            self.computeScore()

            if self.total_score <= 0:
                self.keepPlaying()

    def getAnswer(self):

        self.lastCard = self.card.lastCard()
        self.newCard = self.card.pullFirstCard()

        print(f"The card is: {self.lastCard}")
        while True:
            self.card_guess = input("Higher or Lower? [h/l] or [exit] game: ")
            if self.card_guess.lower() not in ('h', 'l', 'exit'): 
                print(f"Not an apropriate input.")
            else:
                break
        return self.card_guess

    def compareValues(self):

        if not self.is_playing:
            return

        val1 = self.lastCard
        val2 = self.newCard

        if (val2 > val1):
            return 'h'
        if (val2 < val1):
            return 'l'

    def computeScore(self):

        if not self.is_playing:
            return

        points = Points()

        if self.card_guess.lower() == 'exit':  
            self.is_playing = False
            print(f"Thank you for playing hilo. See you.")

        elif self.card_guess.lower() != 'exit': 
            self.score = points.getScore()
            userAnsw = self.card_guess
            compAnsw = self.compareValues()

            if (userAnsw == compAnsw):
                self.score = points.correctScore
            elif (userAnsw != compAnsw):
                self.score = points.incorrectScore

            self.total_score += self.score

            print(f"Next card was: {self.newCard}")
            print(f"Your score is: {self.total_score}\n")
            self.is_playing == (self.score > 0)

    def keepPlaying(self):

        playGame = input("Play game? [y/n] ")

        if playGame.lower() == "y":
            self.is_playing = True
        else:
            self.is_playing = False