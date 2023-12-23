with open('input-4.txt') as f:
    input = [ i.strip() for i in f.readlines() ]

test_input = [
    'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
    'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
    'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
    'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
    'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
    'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
]

def FormatData(input):
    formatted_data = []
    for card_info in input:
        card_details = card_info.split(':')
        numbers = card_details[1].replace('|', '').split()
        formatted_data.append(list(map(int, numbers)))
    return(formatted_data)

def CountDublicates(formatted_data):
    count = []
    for number_list in formatted_data:
        duplicateList = []
        uniqueList = []
        # print(number_list)
        
        for i in number_list:
            if i not in uniqueList:
                uniqueList.append(i)
            elif i not in duplicateList:
                duplicateList.append(i)
        
        #print(duplicateList)
        amount = len(duplicateList)
        count.append(int(amount))
        #print(amount)
        #print(count)
    return(count)

def NumberCalculator(count):
    values = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    sum = 0
    for number in count:
        if 1 <= number <= len(values):
            # Assign the corresponding value based on the index
            result = values[number - 1]
            sum += result
    return(sum)

formatted_data = FormatData(input)
count = CountDublicates(formatted_data)
output = NumberCalculator(count)

print('Part 1:', output)
        
