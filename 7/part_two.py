import re

class File:
    name = ''
    is_dir = False
    size = 0
    contained_files = None
    parent_file = None

    def __init__(self, name, is_dir, size=0):
        self.name = name
        self.is_dir = is_dir
        self.size = size
        self.contained_files = {}

    def calc_size(self):
        # recursive walk of contained files
        if not self.is_dir:
            return self.size
        self.size = 0
        for name, f in self.contained_files.items():
            self.size += f.calc_size()
        return self.size

    def add_file(self, f):
        self.contained_files[f.name] = f
        f.parent_file = self

cd_regex = re.compile('\$ cd (.+)')
ls_regex = re.compile('(.+) (.+)')

with open('input.txt', 'r') as file:
    # line = file.readline().strip()
    root_file = File('/', True)
    current_file = root_file
    for line in [l.strip() for l in file]:
        if line[0] == '$':
            if line[2] == 'l':
                continue
            else:
                change_name = cd_regex.match(line).group(1)
                if change_name == root_file.name:
                    # go to root
                    current_file = root_file
                elif change_name == '..':
                    # go back up one dir
                    current_file = current_file.parent_file
                else:
                    # changing to sub-dir
                    current_file = current_file.contained_files[change_name]
        else:
            # lists a file or directory
            (size_or_dir, name) = ls_regex.match(line).groups()
            new = None
            if size_or_dir == 'dir':
                new = File(name, True)
            else:
                new = File(name, False, int(size_or_dir))
            current_file.add_file(new)

root_file.calc_size()
# total space is 70000000
# need unused space of 30000000
# find the single smallest directory that can be deleted to provide that amount of space
current_available = 70000000 - root_file.size
needed_space = 30000000 - current_available

current_smallest = 70000000
def traverse(file: File):
    global current_smallest
    if file.is_dir:
        if file.size >= needed_space and file.size < current_smallest:
            current_smallest = file.size
        for name, sub_file in file.contained_files.items():
            traverse(sub_file)
traverse(root_file)
print(current_smallest)


