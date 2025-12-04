
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


    def cheapest(self, machine: Machine) -> int:
        a = ((machine.px * machine.by) - (machine.py * machine.bx)) / ((machine.ax * machine.by) - (machine.bx * machine.ay))
        int_a = int(a)
        #print(f"for machine {machine}: got a={a} and int_a={int_a}")
        if a != int_a:
            #print(f"int_a != a -- returning -1")
            return -1
        b = (machine.px - (int_a * machine.ax)) / machine.bx
        int_b = int(b)
        #print(f"for machine {machine}: got b={b} and int_b={int_b}")
        if b != int_b:
            #print(f"int_b != b -- returning -1")
            return -1
        return (int_a * 3) + int_b


    def solve(self, filename):
        self.read_file(filename)
        total = 0
        for machine in self.machines:
            #print(f"machine is {machine}")
            min_cost = self.cheapest(machine)
            if min_cost != -1:
                total += min_cost
        print(f"total min cost is {total}")


if __name__ == "__main__":
    solution = Solution()
    solution.solve('input.txt')
