tests = int(input(""))
for i in range(tests):
    members,voters = map(int, input().split())
    if voters%2==0 :
        print(voters//2+1)
    else:
        print((voters+1)//2)