s = input()
if '.' in s:
    a, b = s.split('.')
else:
    a, b = s, ''

n = int(a) if a else 0
f = int(b) if b else 0
d = 10 ** len(b)

res = bin(n)[2:] + '.'
for _ in range(1000):
    f *= 2
    res += str(f // d)
    f %= d

print(res)
