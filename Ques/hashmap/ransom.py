def canConstruct(ransomNote, magazine) -> bool:
    st1 , st2 = Counter(ransomNote), Counter(magazine)
    if st1 & st2 == st1:
        return True 
    return False
