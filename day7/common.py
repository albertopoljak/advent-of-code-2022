from typing import Optional, Set


class File:
    def __init__(self, filename: str):
        self._filename = filename
        self._filesize = int(self._filename.split(" ")[0])

    @property
    def filename(self):
        return self._filename

    @property
    def filesize(self):
        return self._filesize

    def __hash__(self):
        return hash(self._filename)


class Directory:
    def __init__(self, name: str, parent: Optional["Directory"]):
        self.name = name
        self.parent = parent
        self.files: Set[File] = set()
        self.directories: Set["Directory"] = set()

    @property
    def size(self) -> int:
        return sum(file.filesize for file in self.files) + sum(directory.size for directory in self.directories)

    def directly_contains_directory(self, directory_name: str) -> bool:
        return any(directory.name == directory_name for directory in self.directories)

    def get_subdirectory(self, directory_name: str) -> Optional["Directory"]:
        for directory in self.directories:
            if directory.name == directory_name:
                return directory

    def get_root(self) -> "Directory":
        parent = self.parent
        while parent is not None:
            parent = parent.parent

        return parent

    def get_or_create_subdirectory(self, name: str) -> "Directory":
        subdirectory = self.get_subdirectory(name)
        if not subdirectory:
            subdirectory = Directory(name=name, parent=self)
            self.directories.add(subdirectory)

        return subdirectory

    def _get_absolute_path(self) -> str:
        absolute_path = [self.name]
        parent = self.parent
        while parent is not None:
            absolute_path.append(parent.name)
            parent = parent.parent

        return "".join(reversed(absolute_path))

    def __str__(self):
        return f"/ {self.name} ({self.size})"

    def __hash__(self):
        return hash(self._get_absolute_path())

    def visualize(self, indent_level: int = 0) -> str:
        indent = " " * indent_level
        visualization = [f"{indent}{self}"]
        visualization.extend(f"{indent}{file.filename}" for file in self.files)
        for directory in self.directories:
            visualization.append(directory.visualize(indent_level=indent_level + 4))

        return "\n".join(visualization)

    def get_all_directories(self) -> Set["Directory"]:
        all_subdirectories = set()
        for directory in self.directories:
            all_subdirectories.add(directory)
            all_subdirectories.update(directory.get_all_directories())

        return all_subdirectories


class CommandLine:
    CD_COMMAND = "$ cd "
    CD_COMMAND_MOVE_OUT = ".."
    LS_COMMAND = "$ ls"
    DIR_MARKER = "dir "

    def build_root_directory(self) -> Directory:
        root_directory = Directory(name="/", parent=None)

        with open("input1.txt") as f:
            f.readline()  # skip the first, root ,directory
            command_lines = f.read().split("\n")

        current_directory = root_directory
        for command_line in command_lines:
            if command_line.startswith(self.CD_COMMAND):
                directory_name = command_line.replace(self.CD_COMMAND, "")
                if directory_name == self.CD_COMMAND_MOVE_OUT:
                    current_directory = current_directory.parent
                else:
                    subdirectory = current_directory.get_or_create_subdirectory(directory_name)
                    current_directory = subdirectory
            elif command_line.startswith(self.LS_COMMAND):
                continue
            elif command_line.startswith(self.DIR_MARKER):
                directory_name = command_line.replace(self.DIR_MARKER, "")
                current_directory.get_or_create_subdirectory(directory_name)
            else:
                # files
                current_directory.files.add(File(command_line))

        return root_directory
