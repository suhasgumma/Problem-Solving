import math 
  
# Function that returns True if n  
# is prime else returns False  
def isPrime(n): 
      
    # Corner cases  
    if(n <= 1): 
        return False
    if(n <= 3): 
        return True
      
    # This is checked so that we can skip  
    # middle five numbers in below loop  
    if(n % 2 == 0 or n % 3 == 0): 
        return False
      
    for i in range(5,int(math.sqrt(n) + 1), 6):  
        if(n % i == 0 or n % (i + 2) == 0): 
            return False
      
    return True
  
# Function to return the smallest  
# prime number greater than N  
def nextPrime(N): 
  
    # Base case  
    if (N <= 1): 
        return 2
  
    prime = N 
    found = False
  
    # Loop continuously until isPrime returns  
    # True for a number greater than n  
    while(not found): 
        prime = prime + 1
  
        if(isPrime(prime) == True): 
            found = True
  
    return prime 


def solve():
    d = int(input())

    if d == 1:
        print(6)
        return

    if d%2 == 0:
        f1 = nextPrime(d)
    else:
        f1 = nextPrime(d+1)
    
    f2 = nextPrime(f1+d-1)

    print(f1*f2)
    
    return


t = int(input())




for _ in range(t):
    solve()