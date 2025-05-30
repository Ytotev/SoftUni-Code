budget = float(input())
price_of_flour_1kg = float(input())

price_pack_of_eggs = price_of_flour_1kg * 0.75  # is 75 % of the price for 1 kg flour.
price_of_milk_250g = (price_of_flour_1kg + price_of_flour_1kg * 0.25) / 4  # is 25 % more than the price for 1 kg flour.
# Keep in mind that you use only 250ml milk for a bread.
price_of_bread = price_of_flour_1kg + price_pack_of_eggs + price_of_milk_250g
bread_to_bake = int(budget // price_of_bread)
money_left = budget % price_of_bread

colored_eggs = 0

for current_bread_count in range(1, bread_to_bake + 1):
    colored_eggs += 3
    if current_bread_count % 3 == 0:
        colored_eggs -= current_bread_count - 2
print(
    f'You made {bread_to_bake} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.')
