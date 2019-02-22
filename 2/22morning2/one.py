a = int(input("请输入一个数:"))
sum = 0
s = 1
for i in range(1,a+1):
    s = s *i
    sum += s
print("阶乘之和:",sum)