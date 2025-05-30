number = int(input())

prime_number = True

for divider in range(2, number):
    if number % divider == 0:
        prime_number = False
        break
print(prime_number)
