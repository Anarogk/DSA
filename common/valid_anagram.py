'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    dic = dict()
    for i in s:
        dic[i]+=1
    for j in t:
        dic[j]-=1
    
    for i in dic.values():
        if i != 0:
            return False
    return True

def is_anagram2(s, t):
    if len(s) != len(t):
        return False
    dic1 = {}
    dic2 = {}
    
    for i in s:
        if i in dic1:
            dic1[i]+=1
        else:
            dic1[i] = 1
    for j in t:
        if j in dic2:
            dic2[j]+=1
        else:
            dic2[j] = 1
    for k in dic1:
        if k not in dic2 or dic1[k] != dic2[k]:
            return False
    return True