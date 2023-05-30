list=[]
def prime():
    for i in range(2,X+1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            list.append(i)
    for k in range(0,len(list)):
        Z=X-int(list[k])
        for l  in list:
            if(Z==l):
                print(Z,list[k])
            else:
                pass
X=int(input(""))
prime()