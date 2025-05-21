budget = float(input())
total_amount = 0
current_order = input()
overdraft = False
while current_order != 'End':
    total_amount += int(current_order)
    if total_amount > budget:
        print('You went in overdraft!')
        overdraft = True
        break
    current_order = input()

if not overdraft:
    print('You bought everything needed.')
