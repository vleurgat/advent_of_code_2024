

def validate(target, nums):
    results = []
    for i in range(len(nums)):
        if i == 0:
            results.append(nums[i])
            continue
        newResults = []
        for r in results:
            newResults.append(r + nums[i])
            newResults.append(r * nums[i])
            newResults.append(int(f"{r}{nums[i]}"))
        results = newResults
    #print(f"results are {results} for target {target}")
    return target in results


def solve():
    total = 0
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            sl = line.strip().split(':')
            target = int(sl[0])
            nums = list(map(int, sl[1].strip().split(' ')))
            #print(f"target is {target}; numbers are {nums}")
            
            if validate(target, nums):
                total += target
    print(f"total is {total}")

if __name__ == "__main__":
    solve()
