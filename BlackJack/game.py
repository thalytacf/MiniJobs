import random


class Game:

    def __init__(self):
        self. list_cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.dict_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,
                            'K': 10, 'A': 11}


    def _give_cards(self):
        self.first_card = random.choice(self.list_cards)
        return print(f'Primeira carta: {self.first_card}')


    def _general_rules_(self, choice, first_card):
        amount = 0
        for i in self.dict_values:
            if i == choice:
                if i == 'A':
                    if amount == 0:
                        amount = amount + 11
                    elif amount != 0:
                        if first_card == 'J':
                            amount = amount + 11
                        elif first_card == 'Q':
                            amount = amount + 11
                        elif first_card == 'K':
                            amount = amount + 11
                        elif first_card == 'A':
                            amount = amount + 11
                    else:
                        amount = amount + 1
                else:
                    amount = amount + self.dict_values[i]
            self.score = amount
            return print(f"Valor: {amount}")


    def _turn_cards(self, rules):
        qnt = 1
        while(qnt>0):
            turn_card = int(input('Virar carta?(1-sim/0-não):'))
            if turn_card == 1:
                self.choice = random.choice(self.list_cards)
                print(f'Carta virada:{self.choice}')
                print(f'SCORE: {rules}')
                #importar rules para a marcação do score
            else:
                qnt = qnt - 1