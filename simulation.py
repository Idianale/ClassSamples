#!/bin/python 

import random 

pulls = 100
count = 0
chance = 2
ssr = 0
pulledAt = [0]*100

for i in range(0, pulls):
    count+=1
    pulls=random.randint(1,100)
    if count > 50: 
        chance = 2 * (count - 49)
    if pulls < chance: 
        ssr += 1
        chance = 2
        pulledAt[count] += 1
        count = 0
Sum = 0

print("in", pulls, " rolls")

for i in range(1, 100):
    Sum += pulledAt[i]
    print('{:>3}'.format(i), " rolls got ", '{:>4}'.format(pulledAt[i])," SSRs ", 
    '{:>5}'.format(Sum), "SSRs so far, making it for ", '%.3f' % (Sum / ssr * 100), 
    "% of the SSRs found ")