import random


from BlackJack.dao.cards_dao import CardsDao
from BlackJack.model.cards_model import Cards

class Rules(Cards,CardsDao):

    def menu_play(self):
        menu = f'''
                ************************************************************
                                 BlackJack - You ready? Go!
                ************************************************************
                '''
        return menu

    def random_choice_card(self) -> list:
        self.chosen = random.choice(self.list_cards_and_values)
        return self.chosen

    def rulesA(self):
        if self.score == 0:
            self.score = self.score + 11
        elif self.score != 0:
            if  == 'J' or  == 'Q' or  == 'K' or  == 'A':
                self.score = self.score + 11
            else:
                self.score = self.score + 1
        return self.score

    del rules_general(self, card):
        if card == 'A':
            rules_A_(score)