tests = int(input(""))
for i in range(tests):
    N,K,L  = map(int,input().split())
    songs = []
    for i in range(N):
        length,language = map(int, input().split())
        if language==L:
            songs.append(length)
    if len(songs)<K:
        print(-1)
        continue
    songs.sort(reverse=True)
    Max = sum(songs[:K])
    print(Max)