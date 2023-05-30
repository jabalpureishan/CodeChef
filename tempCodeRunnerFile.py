
def DecToBin(X):
    list=[]
    while(X>0):
        list.append(X%2)
        X=X//2
    print(list)
X=int(input(""))
DecToBin(X)
        