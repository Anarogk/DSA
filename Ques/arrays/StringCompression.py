# Given an array of characters chars, compress it using the following algorithm:
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input 
# character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
# After you are done modifying the input array, return the new length of the array.

def compress (chars) -> int:
    se = set(chars[0])
    count = 1
    char_count = 1
    for i in range(len(chars)):
        if chars[i] in se:
            count+=1
        elif chars[i] not in se: 
            char_count +=2
            chars[char_count-1] = str(chars[i])
            chars[char_count] = str(count)
            se.add(chars[i])
            count = 1
        
        return char_count
