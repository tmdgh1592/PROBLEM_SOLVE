def solution(players, callings):
    players_dict = {player : i for i, player in enumerate(players)}
    race_dict = {i : player for i, player in enumerate(players)}

    for player in callings:
        player_index = players_dict[player]
        front_player = race_dict[player_index - 1]

        players_dict[player] = player_index - 1
        players_dict[front_player] = player_index
        race_dict[player_index - 1] = player
        race_dict[player_index] = front_player

    a = sorted(race_dict.items(), key = lambda item : item[0])
    return [p[1] for p in a]

