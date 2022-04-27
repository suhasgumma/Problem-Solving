T = int(input())

for _ in range(T):
    N, K = map(int, input().split())

    answer = ''

    for _ in range(N):
        dist = int(input())

        if dist%K == 0:
            answer += '1'
        else:
            answer+= '0'
    
    print(answer)