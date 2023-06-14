tests = int(input(""))
for i in range(tests):
    length = int(input(""))
    Om = list(map(int, input().split()))
    Addy = list(map(int, input().split()))
    Om.append(0)
    Addy.append(0)
    MaxOm,MaxAddy = 0,0
    count = 0
    for i in Om:
        if i!=0:
            count += 1
        else:
            MaxOm = max(MaxOm,count)
            count = 0
    count = 0
    for i in Addy:
        if i!=0:
            count += 1
        else:
            MaxAddy = max(MaxAddy,count)
            count = 0
    #print(MaxOm, MaxAddy)
    if MaxOm>MaxAddy:
        print("OM")
    elif MaxAddy>MaxOm:
        print("ADDY")
    else:
        print("DRAW")
    