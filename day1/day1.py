def solve():
    # read file input.txt and print each line
    in1 = []
    in2 = []
    with open('input.txt') as f:
        for line in f:
            a, b = map(int, line.split())
            in1.append(a)
            in2.append(b)
    #in1 = [3,4,2,1,3,3]
    #in2 = [4,3,5,3,9,3]
    sin1 = sorted(in1)
    sin2 = sorted(in2)
    count = 0
    for i in range(len(sin1)):
        count += abs(sin1[i] - sin2[i])
    print(count)

    counts2 = {}
    for i in range(len(sin2)):
        if sin2[i] in counts2:
            counts2[sin2[i]] += 1
        else:
            counts2[sin2[i]] = 1
    score = 0
    for i in range(len(sin1)):
        if sin1[i] in counts2 and counts2[sin1[i]] > 0:
            score += (sin1[i] * counts2[sin1[i]])
    print(score)

if __name__ == "__main__":
    solve()
