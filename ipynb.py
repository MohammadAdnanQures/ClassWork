#!/usr/bin/env python
# coding: utf-8

# #Assignment 1 BuildInFunctionsOfPython 

# # SLICE 
# ##### used to get the substring from a string. have 3 parameters start,stop,step. we can iterate substring using different following methods

# In[56]:


str1 = "this Is A String"
temp = str[0:11:3]
print('First Method \t: ',temp)
print('Second \t\t: ',str1[-1:-11:-2])
temp2 = slice(1,15,4)
print('Third \t\t: ',str1[temp2])
print('Fourth \t\t: ', str1[:])
print('fivth \t\t: ', str1[:11:2])
string_Array = ['p','y','t','h','o','n']
print('Sixth \t\t: ',string_Array[0::2])


# # All
# ##### return true or false based on data. can't perform on string
# ##### based on truth table it will return boolean value. 
# ##### 1) if all elements in a array is true it will return 'true'
# ##### 2) if all are false it will return 'false'
# ##### 3) if any of one is false it return 'false'
# ##### 4) in case of empty it will return 'true'

# In[63]:


all_String = ['1','2','3','0']
print(all(all_String))
All_Temp = [1,2,3,4,5,0]
print(all(All_Temp))


# # ZIP
# ##### used to convert two or more array into tuples. number of tuples depend upon minimum length of  array

# In[74]:


str_array1 = ['Four','Three','Two','One']
int_array1 = [1,2,3,4]
temp = zip(str_array1,int_array1)
print(temp)
print(list(temp))
print(tuple(temp))
print(set(temp))
print('we can display zip in three formats List tuples and sets. major difference is brackets and list is mutable while tuple is immutable and set doesnot hold any unorder value plus duplicate' )

temp_arr1 = [1,51]
temp_arr2 = ['a','b','s','xyz','abc']
tmep_arr3 = ['111','222','333','555','444','777']


temp2 = zip(tmep_arr3,temp_arr1,temp_arr2)
print(tuple(temp2))


# # HASH
# ##### used to encrypt the data into fixed size of length. minimize the computation power than integer 
# ##### only apply on immutable string cuz if we apply on mutable we need to matain the table of hash this leads toward high computation power

# In[95]:


hash_temp = (12,1,3,4,11,8)
print(hash(hash_temp))
list_temp = [1,2,3,4]
print(hash(list_temp))


# # Map
# ###### used to get the result of all element in an array or tuple/set

# In[115]:


def Power(b):
    return b*b

arr2 = [4,5,6,7]
print(set(map(Power,arr2)))

