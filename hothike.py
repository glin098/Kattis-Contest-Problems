n = int(input()) # vacation day
hotTemp = 41
temp = [int(i) for i in input().split()]

for x in range(n-2): # 2 hiking days
    i = max(temp[x],temp[x+2])
    if i < hotTemp:
        hotTemp = i
        hotTempIndex = x
        
print(hotTempIndex+1,hotTemp)
