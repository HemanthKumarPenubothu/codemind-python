N=int(input())
        # Code here
for i in range(1, N+1):
            
            #first right triangle
    for j in range(i):
        print(N-j, end=" ")
            
            # for spaces which is filled with integers
    spaces = (N*2)-(i*2) -1
    for j in range(spaces):
        print(N-i+1,end= " ")
                
            # for another right hand side triangle
    for j in range(i, 0, -1):
        if(N-j+1 == 1):
            continue
        else:
            print(N-j+1, end=" ")
            
    print()
                
        # just opposite of the above
for i in range(N-1, 0, -1):
            
            #first right triangle
    for j in range(i):
        print(N-j, end=" ")
            
            # for spaces which is filled with integers
    spaces = (N*2)-(i*2) -1
    for j in range(spaces):
        print(N-i+1,end= " ")
                
            # for another right hand side triangle
    for j in range(i, 0, -1):
        if(N-j+1 == 1):
            continue
        else:
            print(N-j+1, end=" ")
                
    print()

