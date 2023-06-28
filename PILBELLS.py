def run(bells,first,total,mana):
    for i in range(total):
        if i<first:
            mana += 10
        else:
            mana += 5
    if total==bells:
        mana += 20
    return mana

def main():
    Tests = int(input(""))
    while(Tests>0):
        Tests -= 1
        bells,first,total,mana = map(int, input().split())
        print(run(bells,first,total,mana))

main()