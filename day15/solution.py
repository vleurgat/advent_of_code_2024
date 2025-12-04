
class Solution:

    def __init__(self):
        self.grid = []
        self.moves = ""
        self.x = 0
        self.y = 0


    def read_file(self, filename):
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith('#'):
                    self.grid.append(list(line.strip()))
                elif len(line) > 0:
                    self.moves += line.strip()


    def print_grid(self):
        for y in range(len(self.grid)):
            print("".join(self.grid[y]))


    def inbounds(self, x, y) -> bool:
        return x >= 0 and x < len(self.grid[0]) and y >= 0 and y < len(self.grid)


    def find_starting(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                c = self.grid[y][x]
                if c == '@':
                    self.x = x
                    self.y = y
                    print(f"starting pos is [{x},{y}]")
                    return
        raise Exception("failed to find starting pos")


    def move_horizontal(self, dir):
        #print(f"move {dir} from [{self.x},{self.y}]")
        x = self.x + dir
        y = self.y
        c = self.grid[y][x]
        while c != '#' and self.inbounds(x, y):
            #print(f"next grid point at [{x},{y}] is {c}")
            if c == '.':
                row = self.grid[y].copy()
                #print(f"row copy is {"".join(row)}")
                if dir == -1:
                    row[x:self.x] = self.grid[y][x+1:self.x+1]
                else:
                    row[self.x+1:x+1] = self.grid[y][self.x:x]
                row[self.x] = '.'
                #print(f"transformed row copy is {"".join(row)}")
                self.grid[y] = row
                self.x = self.x + dir
                break
            x = x + dir
            c = self.grid[y][x]


    def move_vertical(self, dir):
        #print(f"move {dir} from [{self.x},{self.y}]")
        x = self.x
        y = self.y + dir
        c = self.grid[y][x]
        while c != '#' and self.inbounds(x, y):
            #print(f"next grid point at [{x},{y}] is {c}")
            if c == '.':
                if dir == -1:
                    for i in range(self.y - y):
                        self.grid[y+i][x] = self.grid[y+i+1][x]
                else:
                    for i in range(y - self.y):
                        self.grid[y-i][x] = self.grid[y-i-1][x]
                self.grid[self.y][x] = '.'
                self.y = self.y + dir
                #self.print_grid()
                break
            y = y + dir
            c = self.grid[y][x]


    def move(self):
        for m in self.moves:
            if m == '<':
                self.move_horizontal(-1)
            elif m == '>':
                self.move_horizontal(1)
            elif m == '^':
                self.move_vertical(-1)
            else:
                self.move_vertical(1)
            #print(f"after {m} move")
        self.print_grid()

    
    def calculate_cost(self):
        cost = 0
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                c = self.grid[y][x]
                if c == 'O':
                    cost += (100 * y) + x
        return cost


    def solve(self, filename):
        self.read_file(filename)
        print(f"grid is {self.grid}")
        print(f"moves are [{self.moves}]")
        self.find_starting()
        self.move()
        cost = self.calculate_cost()
        print(f"total cost is {cost}")


if __name__ == "__main__":
    solution = Solution()
    solution.solve('input.txt')
