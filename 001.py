# -*- coding: UTF-8 -*-
#filename：作业一号
#authorby：phantom
print("-----丧心病狂-----")
import random
total=0

for i in range(1,101):
   total=total+1
print("{0}".format(total))

count=0
for row in range(1,11):
    line1=""
    for col in range(1,11):
        count=count+1

        #print("第{0}行,第{1}列.第{2}题\t\t\t".format(row,col,count))
        a = random.randint(0,99)
        b = random.randint(0,99)
        op = random.randint(1,4)
        if op ==1:
            line1=line1+"%d+%d=\t"%(a,b)

        if op ==2:
            line1=line1+"%d-%d=\t"%(a,b)

        if op ==3:
            line1=line1+"%d*%d=\t"%(a,b)

        if op ==4:
            line1=line1+"%d/%d=\t"%(a,b)

    print(line1)
    print("\t")
print("---over---totally{0}questions".format(count))
