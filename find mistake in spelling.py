#!/usr/bin/env python
# coding: utf-8

# In[3]:


#!/usr/bin/env python
# coding: utf-8

# In[9]:


a=input()
import string
aa=list(a.split(' '))
k=0
wrong=[]
k2=0
for i in aa:
    
    if len(i)>=5:
        
        for j in range(0,len(i)-4):
            if not('a' in i[j:j+5] or 'e' in i[j:j+5] or 'i' in i[j:j+5] or 'o' in i[j:j+5] or 'u' in i[j:j+5]or 'y' in i[j:j+5]):
                k=0
                for t in i[j:j+5]:
                    if t in string.punctuation:
                        k=1
                if k==0:
                    if not(i.isupper()):
                        wrong.append(i)
                        break;
                        k=1
    
#listToStr = ' '.join(map(str, wrong)) 
output1=''
#print(listToStr) 
for i in wrong:
    output1=output1+i+' '
print(output1[:-1],end='')


# In[ ]:

