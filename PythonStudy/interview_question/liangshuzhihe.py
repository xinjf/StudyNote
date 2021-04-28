import time


def sum_number(list,target):
    l = []
    for i in range(0,len(list)-1):
        for j in range(i+1,len(list)-1):
            if  list[i]+list[j]==target:
                l.append([i,j])
    return l
s = time.clock()
print(sum_number([1,5,3,4,2,2,6],4))
e = time.clock()
print(e-s)
