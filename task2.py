def is_merge(s, part1, part2):
    sting = part1 + part2
    a = list(part1)
    b = list(part2)

    if sorted(s) != sorted(sting): return False
    for ind, i in enumerate(list(s)):
        if i != s[-1] and i in a and i > a.index(s[ind]):
            return False
        if i != s[-1] and i in b and i > b.index(s[ind]):
            return False

    return True if len(sting) == len(s) else False


print("Halelya")
print(is_merge('codewars', 'code', 'wasr'))
