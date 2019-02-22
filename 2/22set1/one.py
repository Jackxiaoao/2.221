f = open('test.txt','w')
f.close()

f = open('test.txt','w')
f.write('hello world, i am here!')
f.close()

f = open('test.txt','r')
content = f.read(23)
print(content)
f.close()

f = open('test2.txt','w')
f.close()

f = open('test2.txt','w')
f.write(content)
f.close()