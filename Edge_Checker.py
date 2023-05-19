a,b=map(int,input().split())
if a>=1 and b>=1:
    if b==a+1 or b==a-1 or b==10 and a==1 or a==10 and b==1:
        print('Yes')
    else:
        print('No')
else:
    print('No')