
class Solution:

    def __init__(self):
        self.chars = []
        self.freqs = {}
        self.antinodes = []
        self.distinct_antinodes = {}


    def find_frequencies(self):
        for y in range(len(self.chars)):
            for x in range(len(self.chars[0])):
                c = self.chars[y][x]
                #print(f"char at [{x},{y}] is {c}")
                if c != '.':
                    if c not in self.freqs:
                        self.freqs[c] = [[x,y]]
                    else:
                        self.freqs[c].append([x,y])
        #print(f"frequences are {self.freqs}")


    def calc_diff(self, freq, pos_list, i, j):
        xdiff = pos_list[i][0] - pos_list[j][0]
        ydiff = pos_list[i][1] - pos_list[j][1]
        #print(f"{freq} pair is {pos_list[i]}&{pos_list[j]} - xdiff={xdiff} & ydiff={ydiff}")
        return xdiff, ydiff


    def inbounds(self, x, y) -> bool:
        return x >= 0 and x < len(self.chars[0]) and y >= 0 and y < len(self.chars)


    def calc_distinct(self, x, y):
            if x not in self.distinct_antinodes:
                self.distinct_antinodes[x] = [y]
            elif y not in self.distinct_antinodes[x]:
                self.distinct_antinodes[x].append(y)


    def calc_antinodes(self, pos_list, i, xdiff, ydiff):
        x = pos_list[i][0]
        y = pos_list[i][1]
        while self.inbounds(x, y):
            self.antinodes.append([x, y])
            self.calc_distinct(x, y)
            x = x + xdiff
            y = y + ydiff


    def read_file(self, filename):
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                self.chars.append(line.strip())


    def solve(self, filename):
        self.read_file(filename)
        self.find_frequencies()
        for freq in self.freqs:
            pos_list = self.freqs[freq]
            #print(f"for freq {freq} positions are {pos_list}")
            for i in range(len(pos_list)):
                for j in range(i+1, len(pos_list)):
                    xdiff, ydiff = self.calc_diff(freq, pos_list, i, j)
                    self.calc_antinodes(pos_list, i, xdiff, ydiff)
                    self.calc_antinodes(pos_list, j, -xdiff, -ydiff)
        
        #print(f"antinodes are {self.antinodes} - size is {len(self.antinodes)}")
        #print(f"distinct antinodes are {self.distinct_antinodes}")
        total = 0
        for key in self.distinct_antinodes:
            total += len(self.distinct_antinodes[key])
        print(f"total of distinct antinodes is {total}")


if __name__ == "__main__":
    solution = Solution()
    solution.solve(filename='input.txt')
