T=int(input())
for i in range(1,T+1):
    A=input(str())
    B=[]
    SUm=0
    for j in A:
        B.append(j)
    length=len(B)
    for k in range(1,len(B)+1):
        k=(-k)
        Y=B[k]
        Y=int(Y)
        SUm=SUm+Y*(10**(length-1))
    
        length=length-1
    print(SUm)    
        