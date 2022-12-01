with open("input1.txt") as f:
    elf_inputs = f.read().split("\n\n")

largest_elf_calories = 0
largest_elf_index = 0

for elf_index, elf_input in enumerate(elf_inputs):
    current_elf_calories = sum(list(map(int, elf_input.split())))

    if current_elf_calories > largest_elf_calories:
        largest_elf_calories = current_elf_calories
        largest_elf_index = elf_index

print("Elf", largest_elf_index + 1, "has", largest_elf_calories)