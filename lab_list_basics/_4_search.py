n = int(input())
strings_list = []
selected_stings = []
special_word = input()

for number in range(n):
    current_string = input()
    strings_list.append(current_string)
    if special_word in current_string:
        selected_stings.append(current_string)

print(strings_list)
print(selected_stings)