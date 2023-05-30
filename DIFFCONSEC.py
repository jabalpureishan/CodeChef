T=int(input(""))
T=int(T)
for j in range(1,T+1):
    S=str(input())
    count=0
    for i in range(0,len(S)):
        x=S[i]
        if(i+1==len(S)):
            break
        y=S[i+1]
        x,y=int(x),int(y)
        if(x==y):
            count=count+1
    print(count)

    