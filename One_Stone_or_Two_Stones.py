tests = int(input())
for i in range(tests):
    a,b = map(int,input().split())
    if b>=a:
        print("CHEFINA")
    else:
        print("CHEF")