c=0
st=input()
for i in range(0,len(st)):
    c=0
    for j in range(0,len(st)):
        if(i!=j):
            if(st[i]==st[j]):
                c=c+1
            if(c==1):
                break
    if(c==1):
        break
if(c==0):
    print('Unique Number')
else:
    print('Not Unique Number')
