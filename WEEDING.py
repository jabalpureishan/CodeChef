def run(weeds,days,sprays,array):
    if array[-1]+sprays>days+1:
        return "NO"
    return "YES"

def main():
    Tests = int(input(""))
    while(Tests>0):
        Tests -= 1
        weeds,days,sprays = map(int, input().split())
        array = list(map(int, input("").split()))
        print(run(weeds,days,sprays,array))

main()