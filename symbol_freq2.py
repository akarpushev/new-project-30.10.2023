f = open('old_man.txt','r')
for line in f:
    line.encode('utf-8')
    #line = line.strip()
    print(line)

f.close()