with open("input1.txt") as f:
    elf_inputs = f.read().split("\n\n")

elf_total_calories = []

for elf_index, elf_input in enumerate(elf_inputs):
    elf_total_calories.append(sum(list(map(int, elf_input.split()))))

elf_total_calories.sort(reverse=True)
print("Top 3 elves have", sum(elf_total_calories[:3]))
