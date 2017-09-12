import fileinput
import copy

i=0;
for line in fileinput.input():

    arr1=line.split(' ')
    print(arr1)
    if i==0:
       total=arr1[0]
       window=arr1[1]
       i = i + 1
       print(total)
       print(window)
    else:
       arr2=copy.copy(arr1)
       print(arr2)
