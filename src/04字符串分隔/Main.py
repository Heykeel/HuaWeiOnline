import sys

inStr1 = sys.stdin.readline( ).strip('\n')
inStr2 = sys.stdin.readline( ).strip('\n')

inStrAll = [inStr1,inStr2]
for m in range(2):
    inStr = inStrAll[m]
    inStrMat = [inStr[i:i+8] for i in range(0,len(inStr),8)]
    
    for strCell in inStrMat:
        if(len(strCell)!=8):
            strCell = strCell+"0"*(8-len(strCell))
        print(strCell)