from common import CommandLine


root_directory = CommandLine().build_root_directory()

solution = 0
for directory in root_directory.get_all_directories():
    if directory.size <= 100000:
        solution += directory.size

print(solution)
