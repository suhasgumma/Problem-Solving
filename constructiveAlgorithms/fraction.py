'''
https://codeforces.com/problemset/problem/854/A
'''

def solve(n):
    if n%2 != 0:
        first = n//2
        second = n- first

    else:
        res = n//2

        com = (res%2) +1

        first = res-com
        second = res+ com

    return first,second

n = int(input())

a, b = solve(n)

print(a, b)