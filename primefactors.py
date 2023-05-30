from collections import Counter
Cases=int(input(""))
for i in range(0,Cases):
    length=int(input(""))
    String=str(input(""))
    print(Counter(String))