N=int(input())
arr=map(int,input().split())
e = 0
o = 0
for i in arr:
    if i % 2 == 0:
        e += 1
    else:
        o += 1
if o % 2 == 1:
    print(0)
else:
    print(1)
