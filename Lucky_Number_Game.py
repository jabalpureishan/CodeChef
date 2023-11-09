tests = int(input())
for i in range(tests):
    length,bob,alice = map(int,input().split())
    arr = list(map(int,input().split()))
    bc = ac = 0
    for i in arr:
        if i%bob==0:
            bc += 1
        elif i%alice==0:
            ac += 1
    if bc>ac:
        print("BOB")
    else:
        print("ALICE")