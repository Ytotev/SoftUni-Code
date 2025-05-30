quantity_of_decorations = int(input())  # you should buy each time you go shopping
days_left_until_christmas = int(input())
christmas_spirit = 0
total_costs = 0

for current_day in range(1, days_left_until_christmas + 1):
    if current_day % 11 == 0:
        quantity_of_decorations += 2
    if current_day % 2 == 0:  # buy Ornament Sets
        total_costs += 2 * quantity_of_decorations
        christmas_spirit += 5
    if current_day % 3 == 0:  # buy Tree Skirts and Tree Garlands.
        total_costs += (5 + 3) * quantity_of_decorations
        christmas_spirit += 3 +  10
    if current_day % 5 == 0:  # Tree Lights
        total_costs += 15 * quantity_of_decorations
        christmas_spirit += 17
        if current_day % 3 == 0:
            christmas_spirit += 30
    if current_day % 10 == 0:
        christmas_spirit -= 20
        total_costs += 5 + 3 + 15  # tree skirt, garlands, and lights,

if days_left_until_christmas % 10 == 0:
    christmas_spirit -= 30

print(f'Total cost: {total_costs}')
print(f'Total spirit: {christmas_spirit}')
