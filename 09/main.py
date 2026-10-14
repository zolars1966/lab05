import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    t = int(data[0])
    results = []
    idx = 1

    for _ in range(t):
        p1 = int(data[idx]); q1 = int(data[idx + 1])
        p2 = int(data[idx + 2]); q2 = int(data[idx + 3])
        p3 = int(data[idx + 4]); q3 = int(data[idx + 5])
        p4 = int(data[idx + 6]); q4 = int(data[idx + 7])
        idx += 8

        if q1 < 0: p1, q1 = -p1, -q1
        if q2 < 0: p2, q2 = -p2, -q2
        if q3 < 0: p3, q3 = -p3, -q3
        if q4 < 0: p4, q4 = -p4, -q4

        numA = p1 * q2 + p2 * q1
        denA = q1 * q2

        numB = p3 * q4 + p4 * q3
        denB = q3 * q4

        left  = numA * denB
        right = numB * denA

        if left == right:
            results.append("0")
        elif left < right:
            results.append("-1")
        else:
            results.append("1")

    sys.stdout.write(" ".join(results) + "\n")

if __name__ == "__main__":
    solve()