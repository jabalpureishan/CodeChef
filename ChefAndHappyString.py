T=int(input())
for i in range(1,T+1):
    S=input(str())
    for j in S:
        if((j=="a") or (j=="e") or (j=="i") or (j=="o") or (j=="u")):
            count=0
        else:
            S=S.replace(j," ") 
    X=S.split()
    flag=False
    for i in X:
        if(len(i)>2):
            flag=True
        elif(len(i)<=2):
            flag=False
    if flag:
        print("Happy")
    else:
        print("Sad")
