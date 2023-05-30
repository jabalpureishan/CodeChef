T=int(input())
T=int(T)
for i in range(1,T+1):
    A,B,C=input().split()
    A,B,C=int(A),int(B),int(C)
    flag = False
    if(((A+B)%2!=0) or ((B+C)%2!=0) or ((C+A)%2!=0)):
        flag = True
    if(flag):
        print("YES")
    else:
        print("NO")
        