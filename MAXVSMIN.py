T=int(input())
for i in range(1,T+1):
    A=(input()).split()
    B=max(A,key=int)
    C=min(A,key=int)
    B,C=int(B),int(C)
    print(B-C)