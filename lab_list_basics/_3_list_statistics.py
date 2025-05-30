n = int(input())
positive = []
negative = []

for number in range(n):
    current_number = int(input())
    if current_number >= 0:
        positive.append(current_number)
    elif current_number < 0:
        negative.append(current_number)
print(positive)
print(negative)
print(f'Count of positives: {len(positive)}')
print(f'Sum of negatives: {sum(negative)}')