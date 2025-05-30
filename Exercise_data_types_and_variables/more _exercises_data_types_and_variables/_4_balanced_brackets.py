number_of_lines = int(input())

first_bracket = False
for char in range(number_of_lines):
    current_character = input()
    if current_character == '(':
        if not first_bracket:
            first_bracket = True
        else:
            print('UNBALANCED')
            break
    if current_character == ')':
        if not first_bracket:
            print('UNBALANCED')
            break
        else:
            first_bracket = False
else:
    print('BALANCED')
