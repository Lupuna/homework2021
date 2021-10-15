import random

randoms = []

while True:
    try:
        a = int(input())
        b = int(input())
    except ValueError:
        continue
    else:
        break

for i in range (a):
    randoms.append(random.randrange(1, b))
print (randoms)

for i in range (a - 1):
    for j in range (0, a-i-1):
        if randoms [j] > randoms [j + 1]:
            randoms [j], randoms [j + 1] = randoms [j + 1], randoms [j]

for i in range(a):
    print(randoms[i], end=' ')
        
