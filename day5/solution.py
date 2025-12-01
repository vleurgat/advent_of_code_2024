import re


def validate(i, page, pages, rules):
    if not page in rules:
        return True
    page_rules = rules[page]
    for j in range(i):
        if pages[j] in page_rules:
            #print(f"for page {page} in pages {pages} found bad rule for prior page {pages[j]}")
            return False
    return True


def validate_and_fix(pages, rules):
    for i in range(len(pages)):
        page = pages[i]
        if page in rules:
            page_rules = rules[page]
            for j in range(i):
                if pages[j] in page_rules:
                    #print(f"for page {page} in pages {pages} found bad rule for prior page {pages[j]}")
                    fixed = pages.copy()
                    fixed[i], fixed[j] = fixed[j], fixed[i]
                    return False, fixed
    return True, pages


def calc_middle_sum(updates):
    total = 0
    for update in updates:
        mid = int(len(update) / 2)
        #print(f"for update {update} mid is {mid} and mid value is {int(update[mid])}")
        total += int(update[mid])
    return total


def fix_invalid(updates, rules):
    fixed = []
    for i in range(len(updates)):
        pages = updates[i]
        valid = False
        count = 0
        while not valid and count < 10000:
            valid, pages = validate_and_fix(pages, rules)
            count += 1
        if count >= 10000:
            #print(f"failed for {updates[i]} after {count} attempts")
            return []
        else:
            #print(f"success for {updates[i]} fixed is {pages}")
            fixed.append(pages)
    return fixed


def solve():
    rules_str = []
    updates_str = []
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            if '|' in line:
                rules_str.append(line.strip())
            if ',' in line:
                updates_str.append(line.strip())
    
    rules = {}
    for rule_str in rules_str:
        s = rule_str.split('|')
        key = s[0]
        value = s[1]
        if key in rules:
            rules[key].append(value)
        else:
            rules[key] = [value]
    #print(f"rules are {rules} for {rules_str}")
    
    updates = []
    for update_str in updates_str:
        updates.append(update_str.split(','))
    #print(f"updates are {updates} for {updates_str}")

    valid_updates = []
    invalid_updates = []
    for pages in updates:
        #print(f"working for pages {pages}")
        valid = True
        for i in range(len(pages)):
            if not validate(i, pages[i], pages, rules):
                #print(f"update containing pages {pages} is NOT valid")
                valid = False
                invalid_updates.append(pages)
                break
        if valid:
            #print(f"update containing pages {pages} is valid")
            valid_updates.append(pages)

    #print(f"valid updates are {valid_updates}")
    total = calc_middle_sum(valid_updates)
    print(f"total of middle pages is {total}")

    fixed = fix_invalid(invalid_updates, rules)
    total = calc_middle_sum(fixed)
    print(f"total of fixed middle pages is {total}")


if __name__ == "__main__":
    solve()
