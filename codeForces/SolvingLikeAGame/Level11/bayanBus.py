def listToStr(arr):
    res = ''
    for i in arr: res+= i

    return res


def solve(k):
    border = "+------------------------+"

    row1 = list("|" + ("#."*11) + "|D|)")

    row2 = list("|" + ("#."*11) + "|.|")

    row4 = list("|" + ("#."*11) + "|.|)")

    row3 = list("|#.......................|")

    rem = k

    
    if rem == 1:
        row1[1] = "O"
        rem = 0
    
    if rem == 2:
        row1[1] = "O"
        row2[1] = "O"
        rem = 0
    
    if rem == 3:
        row1[1] = "O"
        row2[1] = "O"
        row3[1] = "O"
        rem = 0

    
    if rem == 4:
        row1[1], row2[1], row3[1], row4[1] = "O", "O", "O", "O"
        rem = 0
    
    if rem == 0:
        row1 = listToStr(row1)
        row2 = listToStr(row2)
        row3 = listToStr(row3)
        row4 = listToStr(row4)
        
        print(border)
        print(row1)
        print(row2)
        print(row3)
        print(row4)
        print(border)
        return
    
    
    if rem > 4:
        row1[1], row2[1], row3[1], row4[1] = "O", "O", "O", "O"
        rem-=4
    
    rowsPossible = rem//3

    rem = rem%3

    pos = 1

    for i in range(1,rowsPossible+1):
        pos = (2*i)+1

        row1[pos] = "O"
        row2[pos] = "O"
        row4[pos] = "O"
    
    pos+=2

    if rem == 1:
        row1[pos] = "O"
    
    if rem == 2:
        row1[pos] = "O"
        row2[pos] = "O"
    
    row1 = listToStr(row1)
    row2 = listToStr(row2)
    row3 = listToStr(row3)
    row4 = listToStr(row4)
    
    print(border)
    print(row1)
    print(row2)
    print(row3)
    print(row4)
    print(border)
    return
    


k = int(input())

solve(k)

