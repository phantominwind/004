# -*- coding: UTF-8 -*-
#filename：作业一号
#authorby：phantom

#print("-----丧心病狂-----")
import random

# 写文件
filename = "homework.txt"
f = open(filename, 'w')  # write 方式第一次写一行

text2write = "nowbegin\n"
f.write(text2write)
f.close()

f = open(filename, 'a') # append 方式读文件





total=0

for i in range(1,101):
   total=total+1
print("{0}".format(total))

count=0
for row in range(1,21):
    line1=""
    for col in range(1,6):
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


    text2write=line1+'\n'
    f.write(text2write)
print("---over---totally{0}questions".format(count))
text2write="---over---totally{0}questions\n".format(count)
f.write(text2write)

f.close()
