def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
a=int(input())

for i in range(a):
    N=int(input())
    factorial=fact(N)
    print(factorial)