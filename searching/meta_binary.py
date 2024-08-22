'''
Approach:

1. Store number of bits to represent the largest array index in variable lg.
2. Use lg to start off the search in a for loop.
3. If the element is found return pos.
4. Otherwise, incrementally construct an index to reach the target value in the for loop.
5. If element found return pos otherwise -1.

'''
import math

def meta_binary_search( arr, key):
    n = len(arr) # len of arr is n

    lg = int(math.log2(n-1)) +1 # Set number of bits to represent largest array index

    pos = 0 
    for i in range(lg-1, -1, -1):
        if arr[pos] == key:
            return pos
        
        new_pos = pos | (1 << i) #Incrementally constructing the index of target value

        if ((new_pos < n) and (arr[new_pos] <= key)): # find element in one direction and update pos
            pos = new_pos

    return pos if arr[pos] == key else -1

def main():
    arr = [3, 4, 5, 6, 2, 9, 10, 18, 4, 3]
    res = meta_binary_search(arr, 4)
    print(res)

