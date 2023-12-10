with open('input-1.txt') as f:
    input = [ i.strip() for i in f.readlines() ]
# input = [
#     '1abc2',
#     'pqr3stu8vwx',
#     'a1b2c3d4e5f',
#     'treb7uchet',
# ]
#print(input)

numbers = []
def CheckNumbers(string):
    numbers = []
    writtenNumbers = [
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
    ]

    for i, word in enumerate(writtenNumbers): # Loop the written numbers
        if word in string: # Check if there is written numbers 
            digit = i + 1
            numbers.append(digit)
    # print('tulos:', numbers, string)
    
    for e in string: # Loop the letters of the input word
        if e.isdigit(): # Check if is number
            numbers.append(e)

    # print('tulos:', numbers, string)
    return numbers

            
# Loop the input    
for string in input:
    digits = []
    
    CheckNumbers(string)

    for i, e in enumerate(string):
        if e.isdigit(): # Check if is number
            digits.append(e)
            
    numbers.append(int(digits[0] + digits[-1])) # Combine first and last letter OR first and first
output = sum((numbers))

print(output)