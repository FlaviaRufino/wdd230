import random

"""This class is responsable for handle the random generation of the cards values."""
    
class Cards:

    def __init__(self):
        self.cardGenerate = random.randint(1, 13)

    def pullFirstCard(self):
        self.cardGenerate = random.randint(1, 13)
        return self.cardGenerate

    def lastCard(self):
        return self.cardGenerate

    

    
        