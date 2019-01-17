from random import random

awardDis = {
    'NO.1':(0, 0.08),
    'NO.2':(0.08, 0.3),
    'NO.3':(0.3, 1.0)
}

def gamble(awardDis):
    record = random()
    for k,v in awardDis.items():
        if v[0] <= record < v[1]:
            return k

results = dict()

for i in range(1000):
    result = gamble(awardDis)
    results[result] = results.get(result,0) + 1

for item in results.items():
    print(item)
