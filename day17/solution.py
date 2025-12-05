import math

class Solution:

    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.program = []
        self.output = []


    def __str__(self) -> str:
        return f"a={self.a} b={self.b} c={self.c}\noutput={self.output}"


    def read_file(self, filename):
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line.startswith("Register A"):
                    self.a = int(line.split(':')[1].strip())
                if line.startswith("Register B"):
                    self.b = int(line.split(':')[1].strip())
                if line.startswith("Register C"):
                    self.c = int(line.split(':')[1].strip())
                if line.startswith("Program"):
                    self.program = list(map(int, line.split(':')[1].strip().split(',')))


    def combo(self, i):
        if i >= len(self.program):
            raise Exception(f"index {i} is out-of-bounds for program of length {len(self.program)}")
        opn = self.program[i]
        if opn >= 0 and opn <= 3:
            return opn
        elif opn == 4:
            return self.a
        elif opn == 5:
            return self.b
        elif opn == 6:
            return self.c
        else:
            raise Exception(f"invalid combo operand {opn}")


    def operand(self, i):
        if i >= len(self.program):
            raise Exception(f"index {i} is out-of-bounds for program of length {len(self.program)}")
        return self.program[i]
    

    def opcode(self, opc, i):
        match opc:
            case 0: # adv
                com = self.combo(i+1)
                den = pow(2, com)
                res = math.floor(self.a / den)
                print(f"adv({opc}) --> floor( a({self.a}) / pow(2, combo({self.program[i+1]}=={com})=={den} ) == {res}")
                self.a = res
                return i+2
            case 1: # bxl
                res = self.b ^ self.operand(i+1)
                print(f"bxl({opc}) -> b({self.b}) ^ lit({self.program[i+1]}) == {res}")
                self.b = res
                return i+2
            case 2: # bst
                com = self.combo(i+1)
                res = com % 8
                print(f"bst({opc}) -> combo({self.program[i+1]}=={com})%8 == {res}")
                self.b = res
                return i+2
            case 3: # jnz
                if self.a == 0:
                    print(f"jnz({opc}) a==0 --> do nothing but skip operand {self.program[i+1]}")
                    return i+2
                res = self.operand(i+1)
                print(f"jnz({opc}) --> jump to {self.program[i+1]} == {res}")
                return res
            case 4: # bxc
                res = self.b ^ self.c
                print(f"bxc({opc}) --> b({self.b}) XOR c({self.c}) == {res}")
                self.b = res
                return i+2
            case 5: # out
                res = self.combo(i+1) % 8
                print(f"out({opc}) --> combo({self.program[i+1]})%8 == {res}")
                self.output.append(res)
                return i+2
            case 6: # bdv
                com = self.combo(i+1)
                den = pow(2, com)
                res = math.floor(self.a / den)
                print(f"bdv({opc}) --> floor( a({self.a}) / pow(2, combo({self.program[i+1]}=={com})=={den} ) == {res}")
                self.b = res
                return i+2
            case 7: # cdv
                com = self.combo(i+1)
                den = pow(2, com)
                res = math.floor(self.a / den)
                print(f"cdv({opc}) --> floor( a({self.a}) / pow(2, combo({self.program[i+1]}=={com})=={den} ) == {res}")
                self.c = res
                return i+2
            case _:
                raise Exception(f"unknown opcode {opc}")


    def execute(self):
        i = 0
        while i < len(self.program):
            opc = self.program[i]
            i = self.opcode(opc, i)
            if self.output != self.program[:len(self.output)]:
                print(f"output is going wrong: {self.output} != {self.program[:len(self.output)]}")
                return


    def solve(self, filename):
        self.read_file(filename)
        print(f"state: {self}")
        print(f"program: {self.program}")
        for i in range(1,100):
            if i%8 != 7:
                continue
            self.a = i
            self.b = 0
            self.c = 0
            self.output = []
            self.execute()
            if i % 1000000 == 0:
                print(f"at i={i}\nstate is: {self}")
            if self.output == self.program:
                print(f"got a matching output for i={i}")
                return


if __name__ == "__main__":
    solution = Solution()
    solution.solve('input.txt')
