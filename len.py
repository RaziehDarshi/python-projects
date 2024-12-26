#!/usr/bin/env python
# coding: utf-8

# In[110]:


s=input()
[m,n]=s.split(' ')
m=int(m)
n=int(n)

#if n==0:
    
#    print('-1 -1')
#if m==0:
 #   print('-1 -1')

pe1=10**(m-1)
pe2=10**m
if m<1:
    print('-1 -1')
elif m==1 and n==0:
    print('0 0')
elif n<1:
    print('-1 -1')
else:
    for i in range(pe1,pe2):
        k=sum(map(int, str(i)))
        #print(i,k)
        if k==n:
            
            l=list(str(i))
            l1=l[::-1]

            ss=''

            for j in range(0,len(l1)):

                ss=ss+l1[j]
 

            l2=int(ss)
          
            print(i,l2)
            kk=3
            break
   
if kk!=3:
    print('-1 -1')




# In[ ]:




