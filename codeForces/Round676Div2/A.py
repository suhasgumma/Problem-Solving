def xor(a, b,x):
    return (a^x) + (b^x)

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    print(a^b)