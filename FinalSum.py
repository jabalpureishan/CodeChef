T=int(input())
for i in range(1,T+1):
    N,Q=input().split()
    A=input().split()
    Sum=0
    for x in A:
      x=int(x)
      Sum=Sum+x
    N,Q=int(N),int(Q)
    for j in range(1,Q+1):
      L=input().split()
      count=0
      for k in range(int(L[0]),int(L[1])+1):
        count = count +1
      if(count%2==0):
        Sum=Sum
      else:
        Sum=Sum+1
    print(Sum)
      

      
      