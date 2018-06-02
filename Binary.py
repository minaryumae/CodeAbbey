#!/bin/python

import sys
n = int(raw_input().strip())
def binary(x):
    if x == 0: return [0]
    binarylist = []
    while x:
        binarylist.append(x % 2)
        x >>= 1
    return binarylist[::-1]

counter = 0
counter_list = []
list = binary(n)
for i in range(len(list)):
    if i + 1 == len(list):
        if list[i] == 1:
            counter += 1
            counter_list.append(counter)
            print max(counter_list)
        else:
            counter_list.append(counter)
            print max(counter_list)
    else:
        if list[i] == 1 :
            counter += 1
        elif list[i] == 0:
            counter_list.append(counter)
            counter = 0

