def count(n):
    sumOfIntegers = sum([int(x) for x in n])
    return sumOfIntegers

while True:
    n = input()
    if n == '0':
        break
    
    m = count(n)
    i = 11;
    
    while(count(str(i*int(n))) != m):
        i = i + 1
    print(i)
