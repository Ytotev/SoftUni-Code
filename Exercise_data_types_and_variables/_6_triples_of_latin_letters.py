# alphbet = 'abcdefghijklmnopqrtsufwxyz'
# number = int(input())
#
# for char1 in range(number):
#     for char2 in range(number):
#         for char3 in range(number):
#             print(alphbet[char1] + alphbet[char2] + alphbet[char3])
# print(alphbet[char2], end='')
# print(alphbet[char3], end='')
# print()

# number = int(input())
#
# for char1 in range(number):
#     for char2 in range(number):
#         for char3 in range(number):
#             print(f'{chr(97 + char1)}{chr(97 + char2)}{chr(97 + char3)}')

# drug variant

number_of_simbols = int(input())

for first_simbolr in range(97, 97 + number_of_simbols): # first letter in Latin alphabet 'a' ASCII = 97
    for second_simbolr in range(97, 97 + number_of_simbols):
        for third_simbolr in range(97, 97 + number_of_simbols):
            print(f'{chr(first_simbolr)}{chr(second_simbolr)}{chr(third_simbolr)}')
