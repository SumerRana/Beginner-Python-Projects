from random import randint

datalist=[]

for i in range(1000):
    value = randint(0, 100)
    datalist.append(value)

with open('ungroupedData.txt', 'w') as f:
    for item in datalist:
        f.write("%s\n" % item)