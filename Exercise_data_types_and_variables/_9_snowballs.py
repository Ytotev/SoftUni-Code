number_of_snowballs = int(input())
best_quality = 0

for snowball in range(number_of_snowballs):
    weight_of_the_snowball = int(input())
    time = int(input())
    quality = int(input())
    current_quality = int(weight_of_the_snowball / time) ** quality
    if current_quality > best_quality:
        best_quality = current_quality
        snowball_weight = weight_of_the_snowball
        snowball_time = time
        snowball_value = current_quality
        snowball_quality = quality
print(f"{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})")
