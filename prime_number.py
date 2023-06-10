n=int(input())
c=0
for i in range (2,n):
    if(n%i==0):
        print("not a prime")
        break
else:
    print("prime")