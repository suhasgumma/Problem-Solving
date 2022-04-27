def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


def canFormPair(s1, s2):

    if len(s1) < len(s2):
        smallS, largeS = s1, s2
    
    else:
        smallS, largeS = s2, s1
    

    s = len(smallS)
    l = len(largeS)

    q = l//s

    if smallS * q == largeS: return smallS

    if largeS[:s] != smallS: return None

    remS = largeS[s:]

    return canFormPair(remS, smallS)


# print(canFormPair("ab", "abab"))


def solve():
    t = input()
    q = input()

    baseString = canFormPair(t, q)

    

    if baseString == None:
        print(-1)
        return
    
    lBs = len(baseString)
    
    if len(t) < len(q):
        smallS, largeS = t, q
    
    else: smallS, largeS = q, t

    l = len(largeS)
    s = len(smallS)

    if l%s != 0:
        a = l//lBs
        b = s//lBs

        lcm = compute_lcm(a, b)

        q = lcm//a

        print(largeS*q)

        return
    
    # q = l//s

    print(largeS)

    return

t = int(input())

for _ in range(t):
    solve()