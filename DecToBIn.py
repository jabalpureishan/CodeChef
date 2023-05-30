
def DecToBin(X):
    list=[]
    while(X>0):
        list.append(X%2)
        X=X//2
    list.reverse()
    for i in list:
        print(i,end="")
X=int(input(""))
DecToBin(X)
        