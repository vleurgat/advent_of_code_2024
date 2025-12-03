
class Solution:

    def __init__(self):
        self.plants = []
        self.regions = []
        self.visited = {}


    def read_file(self, filename):
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                self.plants.append(line.strip())


    def inbounds(self, x, y) -> bool:
        return x >= 0 and x < len(self.plants[0]) and y >= 0 and y < len(self.plants)


    def record_visit(self, x, y):
        if not x in self.visited:
            self.visited[x] = []
        if not y in self.visited[x]:
            self.visited[x].append(y)


    def is_visited(self, x, y) -> bool:
        if x in self.visited:
            return y in self.visited[x]
        return False


    def walk(self, x, y, region):
        #print(f"walk at [{x},{y}] with region {region}")
        if not self.inbounds(x, y):
            #print("  return out-of-bounds")
            return
        if self.is_visited(x, y):
            #print("  return already visited")
            return
        target = ''
        if len(region) > 0:
            target = self.plants[region[0][1]][region[0][0]]
            #print(f"  existing region gives target of {target}")
        if target == '' or target == self.plants[y][x]:
            target = self.plants[y][x]
            region.append([x,y])
            self.record_visit(x, y)
            #print(f"  extended region with [{x},{y}]")
            self.walk(x+1, y, region)
            self.walk(x-1, y, region)
            self.walk(x, y+1, region)
            self.walk(x, y-1, region)


    def calc_perimeter(self, region):
        perimeter = 0
        for r in region:
            x = r[0]
            y = r[1]
            if [x+1,y] not in region:
                perimeter += 1
            if [x-1,y] not in region:
                perimeter += 1
            if [x,y+1] not in region:
                perimeter += 1
            if [x,y-1] not in region:
                perimeter += 1
        return perimeter


    def add_side_point(self, sides, xy, a, b):
        if not xy in sides:
            sides[xy] = {}
        if not a in sides[xy]:
            sides[xy][a] = []
        if not b in sides[xy][a]:
            sides[xy][a].append(b)
            sides[xy][a].sort()


    def count_sides(self, sides) -> int:
        total = 0
        for k1 in sides:
            for k2 in sides[k1]:
                prior_sp = -1
                side_points = sides[k1][k2]
                for sp in side_points:
                    if prior_sp == -1 or (prior_sp+1 != sp):
                        total += 1
                    prior_sp = sp
        return total
    

    def calc_sides(self, region):
        x_sides = {}
        y_sides = {}
        for r in region:
            x = r[0]
            y = r[1]
            if [x-1, y] not in region:
                self.add_side_point(x_sides, x, x-1, y)
            if [x+1, y] not in region:
                self.add_side_point(x_sides, x, x+1, y)
            if [x, y-1] not in region:
                self.add_side_point(y_sides, y, y-1, x)
            if [x, y+1] not in region:
                self.add_side_point(y_sides, y, y+1, x)

        return self.count_sides(x_sides) + self.count_sides(y_sides)


    def find_regions(self):
        for y in range(len(self.plants)):
            for x in range(len(self.plants[0])):
                region = []
                self.walk(x, y, region)
                if len(region) > 0:
                    self.regions.append(region)


    def solve(self, filename):
        self.read_file(filename)
        #print(f"plants are {self.plants}")
        self.find_regions()
        #print(f"regions are: {self.regions}")
        price = 0
        for region in self.regions:
            #perimeter = self.calc_perimeter(region)
            sides = self.calc_sides(region)
            price += len(region) * sides
        print(f"total price is {price}")


if __name__ == "__main__":
    solution = Solution()
    solution.solve('input.txt')
