with open('input-6.txt') as f:
    input = [ i.strip() for i in f.readlines() ]

testinput = ['Time:        38     94     79     70', 'Distance:   241   1549   1074   1091']

# Format the input into four games
def FormatData(input):
    time_line = input[0].split()[1:]
    distance_line = input[1].split()[1:]

    games = []
    for time, distance in zip(time_line, distance_line):
        game = {'time': int(time), 'distance': int(distance)}
        games.append(game)

    return games

def GameAmountOfWins(game):
    #print(f"Game {i}: {game}")
    #print(game['time'], game['distance'])
    game_distance = game['distance']
    game_time = game['time']
    press_time = 0
    speed = 0

    # t = game_time - press_time
    round_wins = 0
    while press_time < game_time:
        press_time += 1
        speed = press_time
        time = game_time - press_time
        distance = time * speed
        if (distance > game_distance):
            round_wins += 1
    return(round_wins)

    #distance = time * speed

formatted_games = FormatData(input)
#GameAmountOfWins(formatted_games[0])

# Loop the games
wins_list = []
for i, game in enumerate(formatted_games, start=1):
    wins_list.append(GameAmountOfWins(game))
print(wins_list)

def MultiplyList(number_list):
    # Multiply elements one by one
    result = 1
    for x in number_list:
        result = result * x
    return result

output = MultiplyList(wins_list)
print('Part 1:', output)