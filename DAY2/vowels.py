# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:58:54 2019

@author: HP
"""
str1 ='aeiouAEIOU'
state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']


result=[]
for i in state_name:
    for x in str1:
        i = i.replace(x,'')
        print(i)
    result.append(i)










s = state_name[0]
for x in state_name:
    for i in x:
        if i in x:
            str2 = x.replace(i,'')
            print(str2)


if(state_name == 'a' and state_name == 'A'):
    state_name[0].remove('a')

elif(state_name == 'e' and state_name == 'E'):
        state_name.remove('e')
        elif(state_name == 'i' and state_name == I):
            state_name.remove('i')
            elif(state_name == 'o' and state_name == 'O'):
                state_name.remove('o')
                elif(state_name == 'u' and state_name == 'U'):
                    state_name.remove('u')
                    print(state_name)
                    
        