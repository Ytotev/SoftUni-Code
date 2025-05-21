number_of_strings = int(input())
char_list = ',._'
string_state = 'pure.'
for string in range(number_of_strings):
    current_string = input()
    for char in char_list:
        if char in current_string:
            string_state = 'not pure!'
    print(f'{current_string} is {string_state}')
