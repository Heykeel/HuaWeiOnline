inStr = input()
inChar= input()

cout = 0
inStr = inStr.lower()
inChar = inChar.lower()
for c in inStr :
    if c == inChar:
        cout+=1
print(cout)