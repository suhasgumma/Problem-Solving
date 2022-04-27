name = input()

curr = 97

res = 0

for dest in name:
    ch1 = abs(curr - ord(dest))

    ch2 = 26 - ch1

    res+= min(ch1, ch2)

    curr = ord(dest)

print(res)

