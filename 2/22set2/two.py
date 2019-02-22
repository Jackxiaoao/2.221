f = open('test.txt','w')
f.close()

f = open('test.txt','w')
f.write('hello i am Wang')
f.close()

f = open('test.txt','r')
num = f.read(15)
print(num)
f.close()

f = open('test2.txt','w')
f.close()

f = open('test2.txt','w')
f.write(num)
f.close()
