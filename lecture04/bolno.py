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
for g in range (a):
    randoms.append (random.randrange (1, b))

def BogoSort(randoms):
    n = len(randoms)
    while (ifi(randoms) == False):
        fif(randoms)

def ifi(randoms):
    n = len(randoms)
    for i in range (0, n-1):
        if (randoms[i] > randoms[i+1]):
         return False
    
def fif(randoms):
    n = len(randoms)
    for i in range (0, n):
        j = random.randrange (0, n-1)
        randoms[i], randoms[j] = randoms[j], randoms[i]

BogoSort(randoms)
for i in range(len(randoms)):
    print (randoms[i], end=' ')
        
    




    

