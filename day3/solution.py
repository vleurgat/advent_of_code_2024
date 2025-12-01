import re


def solve():
    with open('input.txt') as f:
        regex = r"mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don)'t\(\)"
        data = f.read()
        matches = [[x.group(1), x.group(2), x.group(3), x.group(4)] for x in re.finditer(regex, data)]
        #print(f"matches are {matches}")
        total = 0
        do = True
        for mult in matches:
            if mult[2]:
                #print("do is True")
                do = True
            elif mult[3]:
                #print("do is False")
                do = False
            else:
                if do:
                    #print(f"mult {mult[0]} * {mult[1]}")
                    total += (int(mult[0]) * int(mult[1]))
                else:
                    #print(f"NOT mult {mult[0]} * {mult[1]}")
                    total = total
        print(f"total is {total}")


if __name__ == "__main__":
    solve()
