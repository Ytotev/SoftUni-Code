char_number = int(input())
for char in range(1, char_number + 1):
    print('*' * char)

for char in range(char_number - 1, 0, -1):
    print('*' * char)
