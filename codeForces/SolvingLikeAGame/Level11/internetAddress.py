resource = input()

n = len(resource)

curr = 0

res = ''

if resource[0] == "h":
    res+= "http://"
    curr = 4

else:
    res+= "ftp://"
    curr = 3


dom = ""

while resource[curr: curr+2] != "ru":
    dom+= resource[curr]
    curr+=1

if dom == "":
    dom+= resource[curr]
    curr+=1

    while resource[curr: curr+2] != "ru":
        dom+= resource[curr]
        curr+=1

res+= (dom + '.ru')

rem  = resource[curr+2:]

if rem != "": rem = "/" + rem

res+= rem

print(res)