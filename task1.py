a, b, c, d = [int(input()) for i in range(4)]
r = 'ZOMBIE'

if d != 0 and a == 618 and ((b * c) / d).is_integer() and 0 <= ((b * c) / d) <= 10 ** 9:
    r = ((b * c) / d)
elif c != 0 and b == 618 and ((a * d) / c).is_integer() and 0 <= ((a * d) / c) <= 10 ** 9:
    r = ((a * d) / c)
elif b != 0 and c == 618 and ((a * d) / b).is_integer() and 0 <= ((a * d) / b) <= 10 ** 9:
    r = ((a * d) / b)
elif a != 0 and d == 618 and ((b * c) / a).is_integer() and 0 <= ((b * c) / a) <= 10 ** 9:
    r = ((b * c) / a)

print(r)
