n, m, a, b = map(int, input().split())

destroy = n%m

build = m - destroy

dest = destroy* b

bui = build*a

print(min(dest, bui))