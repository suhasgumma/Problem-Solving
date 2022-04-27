def solve():
    n, k, l, c, d, p, nl, np = map(int, input().split())

    nlkl = (k*l)//nl

    cdn = (c*d)

    npp = p//np

    minToasts = min(nlkl, cdn, npp)

    print(minToasts//n)

    return

solve()