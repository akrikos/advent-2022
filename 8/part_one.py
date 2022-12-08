class Tree:
    def __init__(self, height):
        self.height = height
        self.is_visible = False

class Forest:
    def __init__(self, text):
        self.grid = []
        for line in text.split('\n'):
            current_row = []
            self.grid.append(current_row)
            for char in line:
                height = int(char)
                current_row.append(Tree(height))

    def calc_num_visible(self):
        # set trees on the edge as visible
        for x in range(len(self.grid[0])):
            self.grid[0][x].is_visible = True
            self.grid[-1][x].is_visible = True
        for y in range(len(self.grid)):
            self.grid[y][0].is_visible = True
            self.grid[y][-1].is_visible = True

        # from top
        for x in range(len(self.grid[0])):
            highest_seen = 0
            for y in range(len(self.grid)):
                current_tree = self.grid[y][x]
                if current_tree.height > highest_seen:
                    current_tree.is_visible = True
                    highest_seen = current_tree.height

        # from bottom
        for x in range(len(self.grid[0])):
            highest_seen = 0
            for y in range(len(self.grid)-1, -1, -1):
                current_tree = self.grid[y][x]
                if current_tree.height > highest_seen:
                    current_tree.is_visible = True
                    highest_seen = current_tree.height


        # from left
        for y in range(len(self.grid)):
            highest_seen = 0
            for x in range(len(self.grid[0])):
                current_tree = self.grid[y][x]
                if current_tree.height > highest_seen:
                    current_tree.is_visible = True
                    highest_seen = current_tree.height

        # from right
        for y in range(len(self.grid)):
            highest_seen = 0
            for x in range(len(self.grid[0])-1, -1, -1):
                current_tree = self.grid[y][x]
                if current_tree.height > highest_seen:
                    current_tree.is_visible = True
                    highest_seen = current_tree.height

        # add up actual number
        num_visible = 0
        for x in range(len(self.grid[0])):
            for y in range(len(self.grid)):
                current_tree = self.grid[y][x]
                if current_tree.is_visible:
                    num_visible += 1

        return num_visible


# with open('test_input.txt', 'r') as file:
with open('input.txt', 'r') as file:
    f = Forest(file.read())
    print(f'Number of visible trees from outside the forest: {f.calc_num_visible()}')