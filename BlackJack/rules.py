from .game import Game


class Rules:

    def __init__(self):
        self.dict_values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
        self.game = Game()

    def _general_rules_(self):
        for i in self.dict_values:
            if i == self.game.choice:
                if i == 'A':
                    if amount == 0:
                        amount = amount + 11
                    elif amount != 0:
                        if self.game.first_card == 'J':
                            amount = amount + 11
                        elif self.game.first_card == 'Q':
                            amount = amount + 11
                        elif self.game.first_card == 'K':
                            amount = amount + 11
                        elif self.game.first_card == 'A':
                            amount = amount + 11
                    else:
                        amount = amount + 1
                else:
                    amount = amount + self.dict_values[i]
        return print(f"Valor: {amount}")
