n=int(input())
sq=n*n;
cnt=len(str(n))
p=pow(10,cnt)
if (sq%p)==n :
    print('Automorphic Number');
else:
    print('Not an Automorphic Number');