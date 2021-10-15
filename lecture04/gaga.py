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
        
for i in range(a):
    randoms.append(random.randrange(1,b))
print(randoms)
