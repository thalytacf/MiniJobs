import random
from BlackJack.model.cards_model import Cards

class CardsDao(Cards):


    def addiction_values_to_cards(self):
        for x in self.list_cards:
            for y, z in zip(x, self.list_values):
                made_zip = [y, z]
                self.list_cards_and_values.append(made_zip)
        return self.list_cards_and_values