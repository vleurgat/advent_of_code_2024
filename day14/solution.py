
class Solution:

    class Robot:
        def __init__(self):
            self.x = 0
            self.y = 0
            self.vx = 0
            self.vy = 0
            self.max_x = 0
            self.max_y = 0


        def __str__(self):
            return f"[{self.x},{self.y}] vx={self.vx} vy={self.vy}"


        def add(self, s: str, width, height):
            sa = s.split(' ')
            xya = sa[0][2:].split(',')
            va = sa[1][2:].split(',')
            self.x = int(xya[0])
            self.y = int(xya[1])
            self.vx = int(va[0])
            self.vy = int(va[1])
            self.max_x = width -1
            self.max_y = height - 1


        def move(self):
            new_x = self.x + self.vx
            if new_x > self.max_x:
                new_x -= (self.max_x + 1)
            elif new_x < 0:
                new_x += (self.max_x + 1)
            new_y = self.y + self.vy
            if new_y > self.max_y:
                new_y -= (self.max_y + 1)
            elif new_y < 0:
                new_y += (self.max_y + 1)
            #print(f"{self} moving to [{new_x},{new_y}]")
            self.x = new_x
            self.y = new_y


        def quad(self) -> int:
            mid_x = int(self.max_x / 2)
            mid_y = int(self.max_y / 2)
            if self.x < mid_x and self.y < mid_y:
                return 1
            elif self.x > mid_x and self.y < mid_y:
                return 2
            elif self.x < mid_x and self.y > mid_y:
                return 3
            elif self.x > mid_x and self.y > mid_y:
                return 4
            else:
                return 0


    def __init__(self):
        self.robots = []
        self.width = 0
        self.height = 0


    def read_file(self, filename):
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                robot = self.Robot()
                robot.add(line.strip(), self.width, self.height)
                self.robots.append(robot)


    def print_grid(self):
        grid = []
        for y in range(self.height):
            grid.append("." * self.width)
        for robot in self.robots:
            g = grid[robot.y][robot.x]
            if g == '*':
                continue
            if g == '.':
                g = '1'
            else:
                i = int(g)
                if i < 9:
                    i += 1
                    g = f"{i}"
                else:
                    g = '*'
            xl = list(grid[robot.y])
            xl[robot.x] = g
            grid[robot.y] = "".join(xl)
        for y in range(len(grid)):
            print(f"{grid[y]}")


    def solve0(self, filename):
        self.read_file(filename)
        for i in range(1,101):
            print(f"move #{i}")
            for robot in self.robots:
                robot.move()

        self.print_grid()

        quads = {}
        for robot in self.robots:
            q = robot.quad()
            #print(f"robot is in quadrant {q}")
            if q > 0:
                if not q in quads:
                    quads[q] = 0
                quads[q] += 1
        total = 1
        for q in quads:
            print(f"total for quad {q} is {quads[q]}")
            total *= quads[q]
        print(f"total is {total}")


    def possible_tree(self):
        # look for a sequence of at least 10 robots in a line
        rows = {}
        for robot in self.robots:
            x = robot.x
            y = robot.y
            if not x in rows:
                rows[x] = []
            if not y in rows[x]:
                rows[x].append(y)
                rows[x].sort()
        for x in rows:
            if len(rows[x]) >= 10:
                seq = 1
                max_seq = -1
                last = -1
                for y in rows[x]:
                    if last != -1:
                        if last == (y - 1):
                            seq += 1
                            if seq > max_seq:
                                max_seq = seq
                        else:
                            seq = 0
                    last = y
                if max_seq >= 10:
                    return True
        return False


    def solve(self, filename):
        self.read_file(filename)
        for i in range(1, 100000):
            for robot in self.robots:
                robot.move()
            if self.possible_tree():
                print(f"possible tree at move #{i}")
                self.print_grid()
                print("hit return to continue:")
                input()


if __name__ == "__main__":
    solution = Solution()
    solution.width = 101
    solution.height = 103
    solution.solve('input.txt')
