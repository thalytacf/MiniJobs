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


lista_cartas = ['2','3','4','5','6','7','8','9','J','Q','K','A']
dicionario_valores = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':9,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
qnt = 1
valor = 0
x = 0
while(qnt>0):
    virar_carta = int(input('Virar carta?(1-sim/0-não):'))
    if virar_carta == 1:
        choice = random.choice(lista_cartas)
        print(choice)

        for i in dicionario_valores:
            if i == choice:
                if i == 'A':
                    if valor == 0:
                        valor = valor + 11
                    else:
                        valor = valor + 1
                else:
                    valor = valor + dicionario_valores[i]
                print(f"Valor: {valor}")
        x += 1

    else:
        qnt = qnt -1
        print(f'Score:{valor}')
