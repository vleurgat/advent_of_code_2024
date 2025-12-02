
class Solution:

    def __init__(self):
        self.stones = []


    def read_file(self, filename):
        with open(filename) as f:
            self.stones = list(map(int, f.readlines()[0].split()))


    def blink(self):
        new_stones = []
        for stone in self.stones:
            s_stone = str(stone)
            even = (len(s_stone) % 2) == 0
            if stone == 0:
                new_stones.append(1)
            elif even:
                mid = int(len(s_stone)/2)
                new_stones.append(int(s_stone[0:mid]))
                new_stones.append(int(s_stone[mid:]))
            else:
                new_stones.append(stone * 2024)
        self.stones = new_stones


    def solve(self, filename):
        self.read_file(filename)
        print(f"starting stones are: {self.stones}")
        for i in range(1, 76):
            self.blink()
            print(f"after blink #{i} there are {len(self.stones)} stones")

        print(f"after {i} blinks, final number of stones is {len(self.stones)}")


if __name__ == "__main__":
    solution = Solution()
    solution.solve(filename='input.txt')
