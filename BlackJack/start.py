'''
As cartas utilizadas e valores serão conforme abaixo:
"2" => 2
"3" => 3
"4" => 4
"5" => 5
"6" => 6
"7" => 7
"8" => 8
"9" => 9
"10" => 10
"A" => 1
"J" => 10
"Q" => 10
"K" => 10

O jogo deverá embaralhar as cartas acima. O jogo deve pedir para o jogador virar uma cartão,
quando ele virar, deverá apresentar o score de acordo com a carta.

Obs.: O "A" terá o valor 1 quando tiver outro número já virado.

Segue exemplo abaixo:
["A"]                                           ==>  11
["A", "J"]                                    ==>  21
["A", "10", "A"]                         ==>  12
["5", "3", "7"]                           ==>  15
["5", "4", "3", "2", "A", "K"]   ==>  25

'''
import random

class Game:

    def __init__(self):
        self.list_cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.dict_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,'K': 10, 'A': 11}
        self.first_card = random.choice(self.list_cards)

    def give_the_first_card(self):
        print(f'Primeira carta: {self.first_card}')
        return self.first_card


    def rules(self):
        for i in self.dict_values:
            if i == choice:
                if i == 'A':
                    if self.first_card == 'J':
                        amount = amount + 11
                    if self.first_card == 'Q':
                        amount = amount + 11
                    if self.first_card == 'K':
                        amount = amount + 11
                    if self.first_card == 'A':
                        amount = amount + 11
                    print(f'Score:{amount}')
                else:
                    amount = amount + 1
            else:
                amount = amount + self.dict_values[i]
            print(f'Score Final:{amount}')


class Play(Game):

    def __init__(self):
        self.game = Game()

    def run_game(self):
        self.game.give_the_first_card()
        qnt = 1
        while (qnt > 0):
            turn_card = int(input('Virar carta?(1-sim/0-não):'))
            if turn_card == 1:
                amount = 0
                choice = random.choice(self.game.list_cards)
                print(choice)
                self.game.rules()
            else:
                qnt = qnt - 1
        print('passou while')


play = Play()
play.run_game()