with open('input1.txt') as f:
    input = [ i.strip() for i in f.readlines() ]
# input = [
#     '1abc2',
#     'pqr3stu8vwx',
#     'a1b2c3d4e5f',
#     'treb7uchet',
# ]

#print(type('1'))
#print(input)

numbers = []
for string in input:
    digits = []
    
    # Check if is number
    for i, e in enumerate(string):
        if e.isdigit():
            digits.append(e)
    
    # Combine first and last letter OR first and first
    numbers.append(int(digits[0] + digits[-1]))
output = sum((numbers))

print(output)
