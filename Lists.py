n=int(input())
list=[]
for j in range(1,n+1):
    C=input(str())
    C=C.split(" ")
    if(C[0]=="insert"):
      list.insert(int(C[1]),int(C[2])) 
    elif(C[0]=="remove"):
      list.remove(int(C[1]))
    elif(C[0]=="append"):
        list.append(int(C[1]))
    elif(C[0]=="sort"):
      list=list.sort()
    elif(C[0]=="print"):
      print(list)
    elif(C[0]=="pop"):
      list=list.pop()
    elif(C[0]=="reverse"):
      list=list.reverse()
    
    