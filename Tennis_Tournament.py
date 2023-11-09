
tests = int(input())
for i in range(tests):
    n = int(input())
    sum_ = ((n-1)*((n-1)+1))//2
    if sum_>=n and sum_%n==0:
        print("YES")
        string = "0"+"1"*(sum_//n)+"0"*(n-(sum_//n)-1)
        for i in range(n):
            print(string)
            string = (string[-1] + string)[:-1]
    else:
        print("NO")
