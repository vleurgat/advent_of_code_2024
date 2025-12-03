
class Solution:

    class Machine:
        def __init__(self):
            self.ax = 0
            self.ay = 0
            self.bx = 0
            self.by = 0
            self.px = 0
            self.py = 0


        def __str__(self):
            return f"A: X+{self.ax} Y+{self.ay} B: X+{self.bx} Y+{self.by} Prize: X={self.px} Y={self.py}"


        def add_a(self, s: str):
            s = s[10:]
            sa = s.split(',')
            sx = sa[0].split('+')
            sy = sa[1].split('+')
            self.ax = int(sx[1])
            self.ay = int(sy[1])


        def add_b(self, s: str):
            s = s[10:]
            sa = s.split(',')
            sx = sa[0].split('+')
            sy = sa[1].split('+')
            self.bx = int(sx[1])
            self.by = int(sy[1])


        def add_p(self, s: str):
            s = s[7:]
            sa = s.split(',')
            sx = sa[0].split('=')
            sy = sa[1].split('=')
            self.px = 10000000000000 + int(sx[1])
            self.py = 10000000000000 + int(sy[1])


    def __init__(self):
        self.machines = []


    def read_file(self, filename):
        with open(filename) as f:
            lines = f.readlines()
            machine = self.Machine()
            for line in lines:
                if line.startswith("Button A:"):
                    machine.add_a(line.strip())
                if line.startswith("Button B:"):
                    machine.add_b(line.strip())
                if line.startswith("Prize:"):
                    machine.add_p(line.strip())
                    self.machines.append(machine)
                    machine = self.Machine()


    def cheapest_pushes(self, machine: Machine) -> int:
        min_cost = -1
        for a in range(101):
            for b in range(101):
                x = (a * machine.ax) + (b * machine.bx)
                y = (a * machine.ay) + (b * machine.by)
                if x == machine.px and y == machine.py:
                    cost = a*3 + b
                    if min_cost == -1 or cost < min_cost:
                        min_cost = cost
        return min_cost


    def solve(self, filename):
        self.read_file(filename)
        total = 0
        for machine in self.machines:
            print(f"machine is {machine}")
            min_cost = self.cheapest_pushes(machine)
            if min_cost != -1:
                total += min_cost
        print(f"total min cost is {total}")


if __name__ == "__main__":
    solution = Solution()
    solution.solve('test.txt')
