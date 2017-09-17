upper_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
players = 16
player_per_match = 4
total_round = 5


def update_blacklist(blacklists, table):
    for i, v in enumerate(table):
        others = table[:i] + table[i+1:]
        blacklists[v] += others
    return blacklists


def get_player_on_table(n, possible):
    import random
    table = random.choice(list(possible))
    for _ in range(n - 1):
        curr = table[-1]
        possible = set(possible) - set(blacklists[curr])
        selected = random.choice(list(possible))
        table += selected
    return table


def get_matchs(match_per_round, rest, blacklists):
    tables = []
    for _ in range(match_per_round):
        table = get_player_on_table(player_per_match, rest)
        blacklists = update_blacklist(blacklists, table)
        rest = set(rest) - set(table)
        tables.append(table)
    return tables, blacklists

player = upper_char[:players]
print(len(player), player)
match_per_round = players / player_per_match
blacklists = {i: i for i in player}

for _ in range(total_round):
    tables, blacklists = get_matchs(match_per_round, player, blacklists)
    print(tables)
