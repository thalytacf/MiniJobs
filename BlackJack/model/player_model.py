

for i in range(qnt):
    player_nick = input(f'Type player_{i + 1} name: ')
    instance_player = GameDao(player_nick)
    list_instances.append(instance_player)
