#!/usr/bin/env python
# coding: utf-8

# In[11]:


a=int(input())
b=int(input())
list1=[]
for i in range(a+1,b):
    check=0
    for j in range(2, i):
        if i%j==0:
            check=1
    if check==0:
        list1.append(str(i))
    check=0
    
print(','.join(list1))

