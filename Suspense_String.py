tests = int(input())
for i in range(tests):
    length= int(input())
    string = input()
    ans = ""
    a = 0
    b = length - 1
    while a<=b:
        if string[a]=="0":
            ans = "0"+ans
        else:
            ans += "1"
        if a<b:
            if string[b]=="0":
                ans += "0"
            else:
                ans = "1" + ans
        a += 1
        b -= 1
    print(ans) 
