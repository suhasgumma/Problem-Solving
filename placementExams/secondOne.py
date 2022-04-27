def secondQues(string):
    res = ''
    for i in string:
        if ord(i) == 90: res+= 'A'

        if ord(i) == 122: res+='a'


        elif 65 <= ord(i) < 90 or 97 <= ord(i) < 122:
            order = ord(i)+1

            if order == 97 or order == 101 or order == 105 or order == 111 or order == 117:
                res+= chr(order).upper()
            
            else: res+= (chr(order))
        
        else: res+= i
    
    
    return res


while True:
    t = input()

    print(ord('{'))

    print(secondQues(t))

try:
    print(firstFactorial(input()))
except: pass