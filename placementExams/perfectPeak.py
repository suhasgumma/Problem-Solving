N  = int(input())

arr = list(map(int, input().split()))

miniArr = [arr[N-1] for i in range(N)]
maxiArr = [arr[0] for i in range(N)]

for i in range(1,N):
    maxiArr[i] = max(arr[i], maxiArr[i-1])

for i in range(N-2, -1, -1):
    miniArr[i] = min(arr[i], miniArr[i+1])


flag = False


for i in range(N):
    if maxiArr[i] == arr[i] and miniArr[i] == arr[i]:
        if i == 0 or i == N-1: continue
        flag = True
        break

if flag: print(1)

else: print(0)



#Garlic

#Onions

#Asaphodita

#Green Chillies

# Coffee ,Tea, 


#AShgourd/Winter melon
#Black Pepper 
#Honey
#Fruits/ Vegetables/ Nuts
#Dried fruits.


