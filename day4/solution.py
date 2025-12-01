
target = "XMAS"

def walk0(chars):
    #print(f"chars[0] is {chars[0]}")
    result = 0
    for y in range(len(chars)):
        for x in range(len(chars[0])):
            #print(f"char at [{x},{y}] is {chars[y][x]}")
            if chars[y][x] == target[0]:
                result += explore0(chars, x, y, [0,-1], 1)
                result += explore0(chars, x, y, [1,-1], 1)
                result += explore0(chars, x, y, [1,0], 1)
                result += explore0(chars, x, y, [1,1], 1)
                result += explore0(chars, x, y, [0,1], 1)
                result += explore0(chars, x, y, [-1,1], 1)
                result += explore0(chars, x, y, [-1,0], 1)
                result += explore0(chars, x, y, [-1,-1], 1)
    print(f"result is {result}")


def explore0(chars, x, y, dir, t):
    #print(f"explore from {x},{y} in dir {dir}")
    newx = x + dir[0]
    newy = y + dir[1]
    if newx < 0 or newy < 0 or newy >= len(chars) or newx >= len(chars[0]):
        # out of bounds
        return 0
    if chars[newy][newx] != target[t]:
        # not XMAS
        return 0
    if t < (len(target) - 1):
        return explore0(chars, newx, newy, dir, t+1)
    return 1


def walk(chars):
    result = 0
    for y in range(len(chars)):
        for x in range(len(chars[0])):
            #print(f"char at [{x},{y}] is {chars[y][x]}")
            if chars[y][x] == 'A':
                result += explore(chars, x, y)
    print(f"result is {result}")


def explore(chars, x, y):
    #print(f"explore from {x},{y}")
    dirs = [[-1,-1], [1,-1], [1,1], [-1,1]]
    points = ['', '', '', '']
    for i in range(len(dirs)):
        newx = x + dirs[i][0]
        newy = y + dirs[i][1]
        if newx < 0 or newy < 0 or newy >= len(chars) or newx >= len(chars[0]):
            # out of bounds
            return 0
        points[i] = chars[newy][newx]
    if ((points[0] == 'M' and points[2] == 'S') or (points[0] == 'S' and points[2] == 'M')) and ((points[1] == 'M' and points[3] == 'S') or (points[1] == 'S' and points[3] == 'M')):
        return 1
    return 0


def solve():
    chars = []
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            chars.append(line.strip())
    walk(chars)


if __name__ == "__main__":
    solve()
