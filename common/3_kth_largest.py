import heapq
def kth_largest1(arr, k):
    for i in range(k-1): # k = 3, k-1 = 2 , it runs 2 times 0 and 1
        arr.remove(max(arr)) # remove(10, 9)
    return max(arr)

def kth_largest2(arr, k):
    arr.sort()
    return arr[-k]

# here for heapq we use negative numbers as min is highest then we pop least ones and 
# positive it with - output.
# main solution 
def kth_largest(arr, k):
    arr = [ -x for x in arr]  # negative the array
    heapq.heapify(arr)  # heapify the array
    for i in range(k-1): # k = 3, k-1 = 2 , it runs 2 times 0 and 1
        heapq.heappop(arr) # pop(10, 9)
    return -heapq.heappop(arr) # return the last element

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(kth_largest1(arr, 3)) # for loop and remove

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(kth_largest2(arr, 3)) # sort and return random access

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(kth_largest(arr, 3)) # heapq pop operations