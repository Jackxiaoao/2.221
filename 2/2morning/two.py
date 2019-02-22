a = 101
b = []
for i in range(a,200):
    if (i % 2 != 0) and (i % 3 != 0) and (i % 5 != 0) and (i % 7 != 0) and (i % 9 != 0) and (i % 11 != 0) and (i % 13 != 0) and (i % 17 != 0):
        b.append(i)
print("101-200之间的素数个数:",len(b),"101-200之间的素数:",b)