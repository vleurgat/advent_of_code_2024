
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
                    line = line.replace('#', '##').replace('.', '..').replace('O', '[]').replace('@', '@.')
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
                #self.print_grid()
                break
            x = x + dir
            c = self.grid[y][x]


    def copy_grid(self) -> list:
        new_grid = []
        for y in range(len(self.grid)):
            new_grid.append(self.grid[y].copy())
        return new_grid
    

    def move_boxes_vertically(self, dir) -> bool:
        #print(f"would move boxes {dir}: from [{self.x,self.y}]")
        connected = []
        can_move = self.connected_boxes(self.x, self.y + dir, dir, connected)
        #print(f"got connected boxes {connected} and can move is {can_move}")
        if not can_move:
            return False
        
        new_grid = self.copy_grid()
        for point in connected:
            new_grid[point[1]][point[0]] = '.'
        for point in connected:
            x = point[0]
            y = point[1]
            c = self.grid[y][x]
            #print(f"  working on connected point {point} with {c} -> new point is [{x},{y+dir}]")
            new_grid[y+dir][x] = c
        self.grid = new_grid
        return True
    

    def connected_boxes(self, x, y, dir, connected) -> bool:
        c = self.grid[y][x]
        if c == '#':
            return False
        elif c == '.':
            return True
        elif c == '[':
            connected.append([x,y])
            connected.append([x+1,y])
            return self.connected_boxes(x, y+dir, dir, connected) and self.connected_boxes(x+1, y+dir, dir, connected)
        elif c == ']':
            connected.append([x,y])
            connected.append([x-1,y])
            return self.connected_boxes(x, y+dir, dir, connected) and self.connected_boxes(x-1, y+dir, dir, connected)

        raise Exception(f"unexpected character at [{x},{y}] - {c}")


    def move_vertical(self, dir):
        #print(f"move {dir} from [{self.x},{self.y}]")
        x = self.x
        y = self.y + dir
        c = self.grid[y][x]
        while c != '#' and self.inbounds(x, y):
            #print(f"next grid point at [{x},{y}] is {c}")
            if c == '.':
                moved = True
                if abs(self.y - y) > 1:
                    moved = self.move_boxes_vertically(dir)
                if moved:
                    self.grid[self.y + dir][x] = self.grid[self.y][x]
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
        self.print_grid()

    
    def calculate_cost(self):
        cost = 0
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                c = self.grid[y][x]
                if c == '[':
                    cost += (100 * y) + x
        return cost


    def solve(self, filename):
        self.read_file(filename)
        self.print_grid()
        print(f"moves are [{self.moves}]")
        self.find_starting()
        self.move()
        cost = self.calculate_cost()
        print(f"total cost is {cost}")


if __name__ == "__main__":
    solution = Solution()
    solution.solve('input.txt')
