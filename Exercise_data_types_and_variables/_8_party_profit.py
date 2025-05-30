group_size = int(input())
days = int(input())
current_coins = 0
food_cost = 2
drinking_water_cost = 3
monster_kill = 20

for current_day in range(1, days + 1):

    if current_day % 15 == 0:
        group_size += 5

    if current_day % 10 == 0:
        group_size -= 2

    current_coins += 50
    current_coins -= 2 * group_size  # 2 coins per companion for food.

    if current_day % 3 == 0:
        current_coins -= drinking_water_cost * group_size
    if current_day % 5 == 0:
        current_coins += monster_kill * group_size
        if current_day % 3 == 0:
            current_coins -= 2 * group_size  # you spend an additional 2 coins per companion

coins = current_coins // group_size
print(f'{group_size} companions received {coins} coins each.')
