with open('input-6.txt') as f:
    input = [ i.strip() for i in f.readlines() ]

testinput = ['Time:        38     94     79     70', 'Distance:   241   1549   1074   1091']
input2 = ['Time: 38947970', 'Distance: 241154910741091']

def FormatData(input): # Format the input into four games
    time_line = input[0].split()[1:]
    distance_line = input[1].split()[1:]

    games = []
    for time, distance in zip(time_line, distance_line):
        game = {'time': int(time), 'distance': int(distance)}
        games.append(game)

    return games

def GameAmountOfWins(game): # Get the amount of wins per round
    game_distance = game['distance']
    game_time = game['time']
    press_time = 0
    speed = 0
    round_wins = 0
    while press_time < game_time:
        press_time += 1
        speed = press_time
        time = game_time - press_time
        distance = time * speed
        if (distance > game_distance):
            round_wins += 1
    return(round_wins)

def MultiplyList(number_list): # Multiply elements one by one
    result = 1
    for x in number_list:
        result = result * x
    return result

# Part 1
formatted_games = FormatData(input)
wins_list = []
for game in formatted_games: # Loop the games
    wins_list.append(GameAmountOfWins(game))
output = MultiplyList(wins_list)
print('Part 1:', output)

# Part 2
game_part2 = FormatData(input2)
for game in game_part2:
    output2 = GameAmountOfWins(game)
    print('Part 2:', output2)