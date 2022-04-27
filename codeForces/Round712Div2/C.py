def isPoss(s, st, a, b , opA, opB):

    if st == 0:
        return isPoss(s, 1, "(", "(", 1, 1)
    
    if st == len(s)-1:
        if opA == 1 and opB == 1:
            return True, a , b
        
        else: return False, None, None

    elif s[st] == '1':
        ch1, ch2 = (False, None, None), (False, None, None)

        ch1 = isPoss(s, st+1, a + "(", b+"(", opA+1, opB+1)

        if opA >0 and opB > 0:
            ch2 = isPoss(s, st+1, a+ ")", b+ ")", opA-1, opB-1)
        
        if st == 1 and ch1[0]:
            print("Yes")
            print(ch1[1])
            print(ch1[2])
            return
        
        if st == 1 and ch2[0]:
            print("Yes")
            print(ch2[1])
            print(ch2[2])
            return

        
        print("NO")
        return
    
    else:
        ch1, ch2 = (False, None, None), (False, None, None)

        if opB > 0:
            ch1 = isPoss(s, st+1, a + "(", b+ ")", opA+1, opB-1)
        
        if opA > 0:
            ch2 = isPoss(s, st+1, a+ ")", b+ "(", opA-1, opB+1)

        if st == 1 and  ch1[0]:
            print("Yes")
            print(ch1[1])
            print(ch1[2])
            return
        
        if st == 1 and ch2[0]:
            print("Yes")
            print(ch2[1])
            print(ch2[2])
            return

        print("NO")
        return


t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    isPoss(s, 0, "", "", 0, 0)
