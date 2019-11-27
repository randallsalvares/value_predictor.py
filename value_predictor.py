#!/usr/bin/env python
# coding: utf-8

# In[34]:


#define a fucntion that will calculate the task of finding the middle value
def value_predictor(l):
    #check if length is of even value and minimum 6 numbers
    if (len(l)>=6) & (len(l)%2==0):
        n_list = sorted(l) #sort the numbers in the list in an ascending fashion
        return(print("The most likely middle value is {:0.1f}".format(sum(n_list)/len(n_list)))) #return middle value
    else: #if the list entered doesnt meet the minimum length of 6 numbers and is not of an even length than prompt user to redo
        print("the list should be of an even length with minimum 6 numbers\n") 
        print("Kindly input correct list again, thank you")
     
        
    
    


# In[35]:


value_predictor([1,2,3])


# In[36]:


value_predictor([2,4,6,7,8,9,11,13])


# In[ ]:




