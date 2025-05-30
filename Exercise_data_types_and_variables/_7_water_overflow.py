# number_of_lines = int(input())
# tank_capacity = 255
# liters_in_tank = 0
#
# for water in range(number_of_lines):
#     new_water = int(input())
#     if liters_in_tank + new_water <= tank_capacity:
#         liters_in_tank += new_water
#     else:
#         print('Insufficient capacity!')
#         continue
#
# print(liters_in_tank)

# Second variant
number_of_lines = int(input())
tank_capacity = 255

for current_water in range(number_of_lines):
    new_water = int(input())
    if tank_capacity < new_water:
        print('Insufficient capacity!')
        continue
    tank_capacity -= new_water

print(255 - tank_capacity)