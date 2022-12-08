class Tree:
    def __init__(self, height):
        self.height = height
        self.is_visible = False
        self.scenic_score = 0

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

    def calc_highest_scenic(self):
        x_size = len(self.grid[0])
        y_size = len(self.grid)
        highest_scenic = 0
        for x in range(x_size):
            for y in range(y_size):
                tree = self.grid[y][x]
                # look up
                up_score = 0
                search_x = x
                search_y = y - 1
                while search_y >= 0:
                    up_score += 1
                    if self.grid[search_y][search_x].height >= tree.height:
                        break;
                    search_y -= 1

                # look down
                down_score = 0
                search_x = x
                search_y = y + 1
                while search_y <= y_size - 1:
                    down_score += 1
                    if self.grid[search_y][search_x].height >= tree.height:
                        break;
                    search_y += 1

                # look right
                right_score = 0
                search_x = x + 1
                search_y = y
                while search_x <= x_size - 1:
                    right_score += 1
                    if self.grid[search_y][search_x].height >= tree.height:
                        break;
                    search_x += 1

                # look left
                left_score = 0
                search_x = x - 1
                search_y = y
                while search_x >= 0:
                    left_score += 1
                    if self.grid[search_y][search_x].height >= tree.height:
                        break;
                    search_x -= 1

                tree.scenic_score = up_score * right_score * down_score * left_score
                if tree.scenic_score > highest_scenic:
                    highest_scenic = tree.scenic_score

        return highest_scenic


with open('input.txt', 'r') as file:
# with open('input.txt', 'r') as file:
    f = Forest(file.read())
    print(f'Number of visible trees from outside the forest: {f.calc_num_visible()}')
    print(f'Max scenic score: {f.calc_highest_scenic()}')