def run(array,length):
    #box = array[0]
    array.sort(reverse=True)
    XOR = array[0]
    count = 1
    for i in range(1,length):
        if XOR>=array[i]:
            XOR = XOR^array[i]
        else:
            count += 1
            XOR = array[i]
    return count

def main():
    Tests = int(input(""))
    while(Tests>0):
        Tests -= 1
        length = int(input(""))
        #string = input("")
        array = list(map(int, input("").split()))
        #X,Y,Z = map(int, input().split())
        print(run(array,length))

main()