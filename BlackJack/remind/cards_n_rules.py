import random

class CardsRules:

    def __init__(self):
        self.list_cards = [['2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A'],
                      ['2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A'],
                      ['2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A'],
                      ['2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A']]

        self.list_dict_values = [{'J':10},{'Q':10},{'K':10},{'A':1},{'2':2},{'3':3},{'4':4},{'5':5},{'6':6},{'7':7},{'8':8},{'9':9},{'10':10}]
        self.amount = 0

    def give_the_first(self):
        first_card = random.choice(list(self.list_dict_values.items())
        print(f'Primeira carta: {first_card}')
        return first_card

    def rules_and_game(self, first):
        self.amount = first[1]
        x = 0
        qnt = 1
        while(qnt>0):
            turn_card = int(input('Virar carta?(1-sim/0-não):'))
            if turn_card == 1:
                choice = random.choice(self.list_cards)
                print(choice)
                choice_in_list = random.choice(choice)
                print(choice_in_list)

                for i in self.dict_values:
                    if i == choice_in_list:

                        else:
                            self.amount = self.amount + self.dict_values[i]
                        print(f'Score: {self.amount}')
                    elif self.amount == 21:
                        print(f"Score Final: {self.amount} - Você venceu!")
                        qnt = qnt - 1
                    elif self.amount > 21:
                        print(f"Score Final: {self.amount} - Você passou de 21!")
                        qnt = qnt - 1
                x += 1

            else:
                qnt = qnt -1
                print(f'Score Final:{self.amount}')
        return self.amount


# game = CardsRules()
# game.rules_and_game()