
class Solution:

    def __init__(self):
        self.chars = []
        self.trailheads = []
        self.found_peaks = {}


    def read_file(self, filename):
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                self.chars.append(line.strip())


    def inbounds(self, x, y) -> bool:
        ret = (x >= 0 and x < len(self.chars[0]) and y >= 0 and y < len(self.chars))
        if ret and self.chars[y][x] == '.':
            ret = False
        return ret


    def walk(self, next_point: list, target_score: int) -> int:
        x = next_point[0]
        y = next_point[1]
        #print(f"@ [{x},{y}] {target_score}")
        if not self.inbounds(x, y):
            #print(f"walked to [{x},{y}] but is out of bounds")
            return 0
        score = int(self.chars[y][x])
        if score != target_score:
            #print(f"walked to [{x},{y}] but score {score} != target {target_score}")
            return 0
        if score == 9:
            #print(f"walked to [{x},{y}] and reached target 9")
            if not x in self.found_peaks:
                self.found_peaks[x] = []
            if not y in self.found_peaks[x]:
                self.found_peaks[x].append(y)
            return 1
        res = 0
        res += self.walk([x+1, y], score+1)
        res += self.walk([x-1, y], score+1)
        res += self.walk([x, y+1], score+1)
        res += self.walk([x, y-1], score+1)
        return res
    

    def find_trailheads(self):
        for y in range(len(self.chars)):
            for x in range(len(self.chars[0])):
                c = self.chars[y][x]
                if c == '0':
                    print(f"got trailhead at [{x},{y}]")
                    self.trailheads.append([x,y])


    def solve(self, filename):
        self.read_file(filename)
        self.find_trailheads()
        total0 = 0
        total1 = 0
        for trailhead in self.trailheads:
            print(f"\n===== walking from {trailhead} ...")
            trailhead_paths = self.walk(trailhead, 0)
            print(f"got {trailhead_paths} paths to peaks from this trailhead")
            trailhead_total = 0
            for key in self.found_peaks:
                trailhead_total += len(self.found_peaks[key])
            print(f"could reach {trailhead_total} peaks from this trailhead")
            self.found_peaks = {}
            total0 += trailhead_total
            total1 += trailhead_paths
        
        print(f"\n***** total distinct peaks result is {total0}")
        print(f"\n***** total paths result is {total1}")


if __name__ == "__main__":
    solution = Solution()
    solution.solve(filename='input.txt')
