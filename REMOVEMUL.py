def run(S,array):
    return (S*(S+1))//2 - sum(array)

def main():
    Tests = int(input(""))
    while(Tests>0):
        Tests -= 1
        S,Q = map(int, input().split())
        array = list(map(int, input("").split()))
        print(run(S,array))

main()