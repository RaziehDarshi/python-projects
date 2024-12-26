#!/usr/bin/env python
# coding: utf-8

# In[125]:


s=input()
[m,n]=s.split(' ')
m=int(m)
n=int(n)
list1=[]

pe1=10**(m-1)
pe2=10**m

if m==1 and n<10:
    print(n,n)
    
elif n==0 and m>1:
    print('-1 -1')
elif n==1:
    print(10**(m-1),10**(m-1))
elif m<1:
    print('-1 -1')
elif m==1 and n>9:
    print('-1 -1')
elif n>m*9:
    print('-1 -1')
else:
    num_nine1=(n)//9
    num_nine=(n-1)//9
    yekan1=(n)%9
    yekan=(n-1)%9
    if num_nine1==m:
        num1=int(num_nine1*'9')
        print(num1,num1)
    elif num_nine1==m-1 and yekan1!=0:
        
        num1=10*int(num_nine1*'9')+yekan1
        num2=list(str(num1))
        num2=num2[::-1]
        num2=''.join(num2)
        print(int(num2),num1)   
    else:  
        if yekan==0:
            
            num1=pe1+int(num_nine*'9')
            num2=int(num_nine*'9')*10**(m-num_nine)+1*10**(m-num_nine-1)
            print(num1,num2)
            #print(5)
        else:
            if num_nine==0:
                num1=pe1+yekan
                num2=(yekan+1)*10**(m-1)
                #print(3)
            else:
                
                
                num1=pe1+yekan*10**(num_nine)+int(num_nine*'9')
                #print(4)
                if yekan==1:
                    #num2=int((num_nine)*'9')*10**(m-num_nine)+9*10**(m-num_nine-1)
                    num2=int(num_nine*'9')*10**(m-num_nine)+(yekan+1)*10**(m-1-num_nine)
                    #print(2)
                    
                else:    
                    num2=int(num_nine*'9')*10**(m-num_nine)+(yekan+1)*10**(m-1-num_nine)
                    #print(1)
             
            
            print(num1,int(num2))


# In[ ]:




