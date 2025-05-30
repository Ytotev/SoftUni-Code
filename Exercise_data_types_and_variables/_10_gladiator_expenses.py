lost_fights_count = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
shield_broken = 0
expenses = 0

for current_fight in range(1, lost_fights_count + 1):
    if current_fight % 2 == 0:
        expenses += helmet_price
    if current_fight % 3 == 0:
        expenses += sword_price
        if current_fight % 2 == 0:
            expenses += shield_price
            shield_broken += 1
            if shield_broken % 2 == 0:
                expenses += armor_price

print(f'Gladiator expenses: {expenses:.2f} aureus')
