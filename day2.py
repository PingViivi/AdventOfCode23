with open('input-2.txt') as f:
    input = [ i.strip() for i in f.readlines() ]

testinput = [
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green ',
]

class Game:
    def __init__(self, data_str):
        self.title, self.game_data_str = map(str.strip, data_str.split(':'))
        self.games = self.parse_game_data()

    def parse_game_data(self):
        games = self.game_data_str.split(';')
        parsed_games = []
        for game_str in games:
            items = game_str.split(',')
            parsed_game = [item.strip() for item in items]
            parsed_games.append(parsed_game)
        return parsed_games

    def __str__(self):
        return f"{self.title}: {self.games}"

game_objects = [Game(game_str) for game_str in input]

# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
def checkPossibleGames(game):
    ispossible = []
    #print(game)
    for rounds in game:
        for string in rounds:
            amount, color = string.split(' ')
            #print(amount)
            if ((color == 'red' and int(amount) > 12) or (color == 'green' and int(amount) > 13) or (color == 'blue' and int(amount) > 14)):
                ispossible.append(False)
            else:
                ispossible.append(True)
    return all(ispossible)

def fewestCubeAmounts(game):
    reds = []
    greens = []
    blues = []
    for rounds in game:
        for string in rounds:
            amount, color = string.split(' ')
            #print(amount)
            if (color == 'red'):
                reds.append(int(amount))
            if (color == 'green'):
                greens.append(int(amount))
            if (color == 'blue'):
                blues.append(int(amount))
    reds.sort()
    greens.sort()
    blues.sort()
    return reds[-1] * greens[-1] * blues[-1]


# Sum all the possible games together
output1 = 0
output2 = []
for i, game in enumerate(game_objects, start=1):
    possible = checkPossibleGames(game.games)
    power = fewestCubeAmounts(game.games)
    output2.append(power)
    
    if (possible):
        output1 += i

output2 = sum(output2)
print('Part 1:', output1)
print('Part 2:', output2)
