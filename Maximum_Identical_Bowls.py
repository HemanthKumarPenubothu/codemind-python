n=int(input())
a=map(int,input().split())
s=sum(a)
for i in range(n,0,-1):
    if(s%i==0):
        print(i)
        break