#!/usr/bin/env python
# coding: utf-8

# In[34]:


a=float(input())
b=float(input())
c=float(input())
delta=b**2-4*a*c
if a==0 and b==0:
    print('IMPOSSIBLE')
elif a==0 and c==0:
    ans1=0
    print(f'{ans1:.3f}')
elif b==0 and c==0:
    ans1=0
    print(f'{ans1:.3f}')
    ans1=0
    print(f'{ans1:.3f}')
elif a==0:
    ans1=-c/b
    print(f'{ans1:.3f}')
elif b==0:
    if a*c<0:
        ans1=-(-c/a)**0.5
        print(f'{ans1:.3f}')
        
    else:
        print('IMPOSSIBLE')
        
elif delta<0:
    print('IMPOSSIBLE')

elif delta==0:
     ans1=-b/(2*a)
     print(f'{ans1:.3f}')
else:
    ans1=(-b-delta**0.5)/(2*a)
    ans2=(-b+delta**0.5)/(2*a)
    if ans1>ans2:
        print(f'{ans2:.3f}')
        print(f'{ans1:.3f}')
    else:
        print(f'{ans1:.3f}')
        print(f'{ans2:.3f}')
    


# In[ ]:





# In[ ]:




