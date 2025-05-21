comand = input()
new_string = ''

while comand != 'End':

    for letter in comand:
        new_string += letter * 2
    if comand != 'SoftUni':
        print(new_string)

    new_string = ''
    comand = input()
