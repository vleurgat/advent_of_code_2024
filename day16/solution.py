
class Solution:

    class Reindeer:

        def __init__(self, other=None):
            if other != None:
                self.x = other.x
                self.y = other.y
                self.dir = other.dir
                self.cost = other.cost
                self.visited = other.visited.copy()
            else:
                self.x = 0
                self.y = 0
                self.dir = 1 # 0 is north; 1 is east; 2 is south; 3 is west
                self.cost = 0
                self.visited = []


        def visit(self, x, y):
            if not [x,y] in self.visited:
                self.visited.append([x,y])


        def was_visited(self, x, y) -> bool:
            return [x,y] in self.visited


        def move(self, new_x, new_y, new_dir) -> bool:
            if abs(new_dir - self.dir) == 2:
                return False
            if self.was_visited(new_x, new_y):
                return False
            self.visit(new_x, new_y)
            self.x = new_x
            self.y = new_y
            if self.dir != new_dir:
                self.cost += 1000
                self.dir = new_dir
            self.cost += 1
            return True


        def __str__(self) -> str:
            return f"x={self.x} y={self.y} dir={self.dir} cost={self.cost}"


    def __init__(self):
        self.grid = []
        self.start_x = 0
        self.start_y = 0
        self.end_x = 0
        self.end_y = 0
        self.min_cost = -1
        self.cost_per_point = {}


    def read_file(self, filename):
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                self.grid.append(line.strip())


    def print_grid(self):
        for y in range(len(self.grid)):
            print(self.grid[y])


    def find_start_and_end(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                c = self.grid[y][x]
                if c == 'S':
                    self.start_x = x
                    self.start_y = y
                    print(f"starting pos is [{x},{y}]")
                if c == 'E':
                    self.end_x = x
                    self.end_y = y
                    print(f"end pos is [{x},{y}]")


    def set_point_cost(self, r : Reindeer):
        ps = f"{r.x},{r.y},{r.dir}"
        if not ps in self.cost_per_point:
            self.cost_per_point[ps] = r.cost
        else:
            cost = self.cost_per_point[ps]
            if cost > r.cost:
                self.cost_per_point[ps] = r.cost


    def point_cost(self, r : Reindeer) -> int:
        ps = f"{r.x},{r.y},{r.dir}"
        if ps in self.cost_per_point:
            return self.cost_per_point[ps]
        return 1000000000


    def walk(self, r : Reindeer):
        print(f"walk {r}")
        context = []
        context.append(r)
        i = 0
        while len(context) > 0:
            i += 1
            if i % 100000 == 0:
                print(f"loop #{i} - length of context is {len(context)}")
            r = context.pop()
            if r.x == self.end_x and r.y == self.end_y:
                print(f"got complete {r}")
                if self.min_cost == -1 or r.cost < self.min_cost:
                    self.min_cost = r.cost
            elif (self.min_cost == -1 or r.cost < self.min_cost) and r.cost < self.point_cost(r):
                self.set_point_cost(r)
                context.extend(self.next_moves(r))


    def next_moves(self, r : Reindeer) -> list:
        moves = []
        if self.grid[r.y-1][r.x] != '#':
            rc = self.Reindeer(r)
            if rc.move(r.x, r.y-1, 0):
                moves.append(rc)
        if self.grid[r.y+1][r.x] != '#':
            rc = self.Reindeer(r)
            if rc.move(r.x, r.y+1, 2):
                moves.append(rc)
        if self.grid[r.y][r.x-1] != '#':
            rc = self.Reindeer(r)
            if rc.move(r.x-1, r.y, 3):
                moves.append(rc)
        if self.grid[r.y][r.x+1] != '#':
            rc = self.Reindeer(r)
            if rc.move(r.x+1, r.y, 1):
                moves.append(rc)
        return moves


    def solve(self, filename):
        self.read_file(filename)
        self.print_grid()
        self.find_start_and_end()
        r = self.Reindeer()
        r.x = self.start_x
        r.y = self.start_y
        self.walk(r)
        print(f"min cost is {self.min_cost}")


if __name__ == "__main__":
    solution = Solution()
    solution.solve('input.txt')
