"""
Kadane's Algorithm 0(n) time and 0(1) space
mainly use maxx for max_so_far and max_end is curr_max or max_now
this is because maxx should never consider gaps from curr max and add curr max to gapped curr_maxx

"""

def kadane(arr, size):
    maxx = float("-inf") # set max to -inf
    max_end = 0 # curr max to 0
    for i in range(0, size): # for i in arr
        max_end = max_end + arr[i] #curr max = curr max + a[i]
        maxx = max(maxx, max_end) # max = max(max, curr max)
        max_end = max(0, max_end) # curr max = max(0, curr max)
    return maxx # return max


a = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum contiguous sum is", kadane(a, len(a)))