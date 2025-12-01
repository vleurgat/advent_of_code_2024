

def turn_right(dir):
    if dir[0] == 0 and dir[1] == -1: # up to right
        return [1, 0]
    if dir[0] == 1 and dir[1] == 0: # right to down
        return [0, 1]
    if dir[0] == 0 and dir[1] == 1: # down to left
        return [-1, 0]
    if dir[0] == -1 and dir[1] == 0: # left to up
        return [0, -1]


def walk(chars, x, y, dir):
    visited = {}
    loopCount = 0
    while loopCount < 10000:
        loopCount += 1
        #print(f"visting [{x},{y}] dir is {dir}")
        if not x in visited:
            visited[x] = []
        if not y in visited[x]:
            visited[x].append(y)

        moved = False
        moveCount = 0
        newx, newy = x, y
        while not moved and moveCount < 5:
            moveCount += 1
            newx = x + dir[0]
            newy = y + dir[1]
            if newx < 0 or newy < 0 or newy >= len(chars) or newx >= len(chars[0]):
                # out of bounds
                #print(f"completed: visited is {visited}")
                return visited
            
            c = chars[newy][newx]
            if c == '#':
                # need to turn
                dir = turn_right(dir)
            else:
                moved = True
        if moveCount >= 5:
            raise Exception("got stuck in a move loop")
        x = newx
        y = newy
    if loopCount >= 10000:
        #print(f"found a loop for the guard")
        return {}


def find_starting(chars):
    for y in range(len(chars)):
        for x in range(len(chars[0])):
            c = chars[y][x]
            #print(f"char at [{x},{y}] is {c}")
            if c == '^':
                return x, y, [0,-1]
            elif c == '>':
                return x, y, [1,0]
            elif c == '<':
                return x, y, [-1,0]
            elif c == 'v':
                return x, y, [0,1]
    raise Exception("failed to find starting pos")


def solve0():
    chars = []
    with open('test.txt') as f:
        lines = f.readlines()
        for line in lines:
            chars.append(line.strip())
    x, y, dir = find_starting(chars)
    print(f"starting position is [{x},{y},{dir}]")
    
    visited = walk(chars, x, y, dir)
    total = 0
    for key in visited:
        total += len(visited[key])
    print(f"distinct positions: {total}")


def solve():
    chars = []
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            chars.append(line.strip())
    sx, sy, dir = find_starting(chars)
    print(f"starting position is [{sx},{sy},{dir}]")
    
    obstacles = []
    for y in range(len(chars)):
        for x in range(len(chars[0])):
            c = chars[y][x]
            if c == '.':
                print(f"try obstacle at [{x},{y}]")
                copy = chars.copy()
                s = list(copy[y])
                s[x] = '#'
                copy[y] = "".join(s)
                visited = walk(copy, sx, sy, dir)
                if len(visited) == 0:
                    obstacles.append(f"[{x},{y}]")
    print(f"obstacles are {obstacles} - len is {len(obstacles)}")


if __name__ == "__main__":
    solve()
