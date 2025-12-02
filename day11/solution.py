
class Solution:

    def __init__(self):
        self.stones = []
        self.max_depth = 0
        self.cache = {}
        self.cache_hits = 0


    def read_file(self, filename):
        with open(filename) as f:
            self.stones = list(map(int, f.readlines()[0].split()))


    def has_even_digits(self, n: int) -> bool:
        count = 0
        while n > 0:
            n = int(n / 10)
            count += 1
        return (count % 2) == 0


    def replacement(self, stone: int) -> list:
        if stone == 0:
            return [1]
        elif self.has_even_digits(stone):
            s_stone = str(stone)
            mid = int(len(s_stone)/2)
            return [int(s_stone[0:mid]), int(s_stone[mid:])]
        else:
            return [stone * 2024]


    def cache_lookup(self, stone, depth):
        if stone in self.cache:
           if depth in self.cache[stone]:
               #print(f"cache hit {stone} @ {depth}")
               self.cache_hits += 1
               return self.cache[stone][depth]
        return -1
    

    def cache_total(self, stone, depth, total):
        if not stone in self.cache:
            self.cache[stone] = {}
        if not depth in self.cache[stone]:
            #print(f"populate cache for {stone} at {depth} with {total}")
            self.cache[stone][depth] = total


    def blinks(self, stone, depth) -> int:
        remainder = self.max_depth - depth + 1
        #print(f"blinks: stone={stone} depth={depth} remainder={rem}")

        total = self.cache_lookup(stone, remainder)
        if total > -1:
            return total

        reps = self.replacement(stone)
        total = 0
        if depth == self.max_depth:
            total = len(reps)
        else:
            for rep in reps:
                total += self.blinks(rep, depth+1)

        self.cache_total(stone, remainder, total)
        return total


    def solve(self, _filename, _max_depth):
        self.read_file(_filename)
        self.max_depth = _max_depth
        print(f"starting stones are: {self.stones}")
        total = 0
        for stone in self.stones:
            subtotal = self.blinks(stone, 1)
            print(f"for stone {stone} got subtotal of {subtotal} for {self.max_depth} blinks")
            total += subtotal
        print(f"after {self.max_depth} blinks, final number of stones is {total} and cache hits is {self.cache_hits}")


if __name__ == "__main__":
    solution = Solution()
    solution.solve('input.txt', 75)
