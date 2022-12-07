from common import CommandLine


root_directory = CommandLine().build_root_directory()


TOTAL_DISK_SPACE = 70000000
NEEDED_DISK_SPACE = 30000000
current_disk_size = root_directory.size
current_size_of_unused = TOTAL_DISK_SPACE - current_disk_size
size_to_delete = NEEDED_DISK_SPACE - current_size_of_unused

directories_eligible_for_deletion = set()


for directory in root_directory.get_all_directories():
    if directory.size >= size_to_delete:
        directories_eligible_for_deletion.add(directory)


print(min(directories_eligible_for_deletion, key=lambda d: d.size))
