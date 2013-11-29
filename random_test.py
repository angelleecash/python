import random

values = [5, 10, 15, 20, 50]

count = 10000000

d = {}

for i in range(count):
    v = random.randrange(100)
    for ti in range(len(values)):
        cv = values[ti]
        if v < cv:
            d[cv] = d.get(cv, 0)+1
            break
        else:
            v -= cv


for k in range(len(values)):
    key=values[k]
    print key, ":", d[key], d[key]*1.0/count*100,"%"
