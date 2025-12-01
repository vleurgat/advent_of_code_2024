
def safe(row, up: bool, skipped = False) -> int:
    print(f"going {'up' if up else 'down'} for row {row} with skipped {skipped}")
    for i in range(len(row)-1):
        cur = row[i]
        next = row[i+1]
        diff = (next - cur) if up else (cur - next)
        #print(f" i is {i} cur is {cur} next is {next} and diff is {diff}")
        if diff > 3 or diff < 1:
            if skipped:
                print("already skipped return 0")
                return 0
            else:
                copy = row.copy()
                del copy[i]
                r = safe(copy, up, True)
                if r != 1:
                    copy = row.copy()
                    del copy[i+1]
                    r = safe(copy, up, True)
                print(f"skipped result return {r}")
                return r
    print("all good return 1")
    return 1


def solve():
    data = []
    with open('input.txt') as f:
        for line in f:
            a = list(map(int, line.split()))
            data.append(a)
    s = 0
    for row in data:
        if len(row) < 2:
            continue
        else:
            if safe(row, True) == 1:
                s += 1
            else:
                s += safe(row, False)
    print(s)


if __name__ == "__main__":
    solve()
