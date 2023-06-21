def run(array):
    a,b = 0,0
    count =0 
    
    for i in array:
        if i=="A":
            a += 1
        elif i=="B":
            b += 1
        elif i=="AB":
            count += 1
        elif i=="O":
            count += 1
    count += max(a,b)
    return count



def main():
    Tests = int(input(""))
    while(Tests>0):
        Tests -= 1
        length = int(input(""))
        array = list(map(str, input("").split()))
        print(run(array))

main()