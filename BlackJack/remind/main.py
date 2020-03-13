import random


list_cards = ['2','3','4','5','6','7','8','9','J','Q','K','A']
dict_values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
qnt = 1
amount = 0
x = 0
first_card = random.choice(list(dict_values.items()))
print(f'Primeira carta: {first_card}')
amount = first_card[1]

while(qnt>0):
    turn_card = int(input('Virar carta?(1-sim/0-não):'))
    if turn_card == 1:
        choice = random.choice(list_cards)
        print(choice)

        for i in dict_values:
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
                    amount = amount + dict_values[i]
                    print(f'Score: {amount}')
            elif amount == 21:
                print(f"Score Final: {amount} - Você venceu!")
                break
            elif amount > 21:
                print(f"Score Final: {amount} - Você passou de 21!")
                break
        x += 1

    else:
        qnt = qnt -1
        print(f'Score Final:{amount}')