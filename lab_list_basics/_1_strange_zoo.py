animal_parts = []

for animal_part in range(3):
    current_part = input()
    animal_parts.append(current_part)

animal_parts[0], animal_parts[-1] = animal_parts[-1], animal_parts[0]

print(animal_parts)