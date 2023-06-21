def run(power,capactiy,cars,outlets,hours):
    total = 0
    capactiy.sort(reverse=True)
    power.sort(reverse=True)
    power.extend([0]*(len(capactiy)-len(power)))
    for i in range(cars):
        total += min(hours*power[i],capactiy[i])
    return total
        

def main():
    Tests = int(input(""))
    while(Tests>0):
        Tests -= 1
        cars,outlets,hours = map(int, input().split())
        capactiy = list(map(int, input("").split()))
        power = list(map(int, input("").split()))
        print(run(power,capactiy,cars,outlets,hours))

main()