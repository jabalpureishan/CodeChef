T=int(input())
for i in range(1,T+1):
    N=int(input())
    A = list(map(int,input("").strip().split()))[:N]
    def most_frequent(A):
        return max(set(A), key = A.count)
    Y=most_frequent(A)
    Z=A.count(Y) 
    print(N-Z)