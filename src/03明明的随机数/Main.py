while True:
    try:
        n = int(input())
        inSet = set()
        for i in range(n):
            inSet.add(int(input()))
    except:
        break
        
    inList = list(inSet)
    outList = sorted(inList)
    for i in outList:
        print(i)