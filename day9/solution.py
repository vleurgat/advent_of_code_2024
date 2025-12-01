
class Solution:

    def __init__(self):
        self.input = ""
        self.disk_map = []


    def read_file(self, filename):
        with open(filename) as f:
            self.input = f.readlines()[0].strip()


    def input_to_disk_map(self):
        is_file = True
        id = 0
        for c in self.input:
            i = int(c)
            if is_file:
                for _ in range(i):
                    self.disk_map.append(id)
                id += 1
            else:
                for _ in range(i):
                    self.disk_map.append(-1)
            is_file = not is_file


    def map_to_str(self, map):
        s = ""
        for m in map:
            if m >=0 and m <= 9:
                s += str(m)
            elif m == -1:
                s += "."
            else:
                s += "X"
        return s


    def find_next_space(self, s, disk_map):
        #print(f"find next space: s={s} and map is {"".join(disk_map)}")
        for i in range(s, len(disk_map)):
            c = disk_map[i]
            if c == -1:
                return i
        return -1


    def find_next_block_space(self, start, target_size, disk_map):
        if start == -1:
            return -1, -1
        #print(f"find next space block of size {target_size}; map is {self.map_to_str(disk_map)}")
        size = 0
        j = -1
        min_space = -1
        for i in range(start, len(disk_map)):
            c = disk_map[i]
            if c == -1:
                if min_space == -1:
                    min_space = i
                if j == -1:
                    j = i
                size += 1
                if size == target_size:
                    #print(f"found space block of size {size} starting at {j}")
                    return j, min_space
            else:
                size = 0
                j = -1
        #print(f"failed to find space block of size {target_size}")
        return -1, min_space


    def compact_disk_map0(self):
        compacted = self.disk_map.copy()
        j = 0
        print(f"compacting map of len {len(self.disk_map)}")
        for i in range(len(self.disk_map)-1, -1, -1):
            if i % 1000 == 0:
                print(f"compacting with index {i} - replacement index is {j}")
            c = self.disk_map[i]
            if c != -1:
                j = self.find_next_space(j, compacted)
                if j >= 0 and j < i:
                    #print(f"compact {i} is not space -- next space is {j} with compacted {self.map_to_str(compacted)}")
                    compacted[i] = -1
                    compacted[j] = c
            if j > i:
                break;
        print(f"compacted disk map is: {self.map_to_str(compacted)}")
        return compacted


    def find_block(self, s):
        c = self.disk_map[s]
        for i in range(s-1, -1, -1):
            if self.disk_map[i] != c:
                return i
        return s-1


    def move_block(self, compacted, from_i, to_i, len):
        #print(f"move block of len {len} from {from_i} to {to_i}")
        for i in range(len):
            compacted[to_i + i] = compacted[from_i - i]
            compacted[from_i - i] = -1


    def compact_disk_map(self):
        compacted = self.disk_map.copy()
        min_space = 0
        print(f"compacting map of len {len(self.disk_map)}")
        i = len(self.disk_map)-1
        while i >= 0:
            if i % 1000 == 0:
                print(f"compacting with index {i}")
            c = self.disk_map[i]
            if c != -1:
                j = self.find_block(i)
                k, min_space = self.find_next_block_space(min_space, (i-j), compacted)
                if k >= 0 and k < i:
                    #print(f"compact {i} is file block of size {i-j} -- next space block is at {k} with compacted {self.map_to_str(compacted)}")
                    self.move_block(compacted, i, k, (i-j))
                if min_space > i:
                    #print(f"min_space {min_space} > i {i} - so not continuing")
                    break;
                i = j
            else:
                i -= 1
        #print(f"compacted disk map is: {self.map_to_str(compacted)}")
        return compacted


    def calc_checksum(self, disk_map):
        sum = 0
        for i, c in enumerate(disk_map):
            if c != -1:
                sum += (i * c)
        print(f"check sum is {sum}")


    def solve(self, filename):
        self.read_file(filename)
        #print(f"input is {self.input}")
        self.input_to_disk_map()
        #print(f"disk_map is {self.map_to_str(self.disk_map)}")
        print(f"disk_map has len {len(self.disk_map)}")
        compacted = self.compact_disk_map()
        self.calc_checksum(compacted)


if __name__ == "__main__":
    solution = Solution()
    solution.solve(filename='input.txt')
