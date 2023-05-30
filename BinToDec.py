
def BinToDec():
    list=[]
    count,n=0,0
    for i in X:
        list.append(i)
    for j in range(1,len(list)+1):
        j=-j
        count=count+ (int(list[j])*(2**n))
        n=n+1
    print(count)
X=input("")

BinToDec()

