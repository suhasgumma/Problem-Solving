try:
    for _ in range(int(input())):
        N = int(input())

        customers = list(map(int, input().split()))

        cashCounter = {5: 0, 10: 0, 15:0}

        can = True

        for i in range(N):
            moneyGiven = customers[i]
            change = moneyGiven - 5

            if change == 0:
                pass

            elif change == 5:
                if cashCounter[5] >= 1:
                    cashCounter[5]-=1
                else:
                    print('NO')
                    can = False
                    break
            
            elif change == 10:
                if cashCounter[10] >= 1:
                    cashCounter[10]-=1

                elif cashCounter[5] >=2:
                    cashCounter[5]-=2
                
                else:
                    print('NO')
                    can = False
                    break
            
            cashCounter[moneyGiven]+=1

        
        if can:
            print('YES')
except:
    pass
