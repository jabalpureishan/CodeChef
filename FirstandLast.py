T=int(input())
for i in range(1,T+1):
    A=input(str())
    B=[]
    for j in A:
        B.append(j)
    for k in range(1,len(B)+1):
        k=(-k)
        print(B[k],end="")