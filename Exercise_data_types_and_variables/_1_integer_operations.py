numbers = []

for number in range(4):
    new_number = int(input())
    numbers.append(new_number)

result = ((numbers[0] + numbers[1]) // numbers[2]) * numbers[3]
print(result)
