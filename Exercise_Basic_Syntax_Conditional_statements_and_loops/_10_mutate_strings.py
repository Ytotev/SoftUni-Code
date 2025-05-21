first_string = input()
second_string = input()
new_string = ''

for letter_number in range(len(first_string)):
    if first_string[letter_number] == second_string[letter_number]:
        continue
    else:
        new_string = second_string[:letter_number] + second_string[letter_number] + first_string[letter_number + 1:]
        print(new_string)
