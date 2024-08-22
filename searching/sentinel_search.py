
'''
Here are the steps involved in the Sentinel Linear Search Algorithm:
1. Set the last element of the array to the target value. This is known as the sentinel value.
2. Set the index variable “i” to the first element of the array.
3. Use a loop to iterate through the array, comparing each element with the target value.
4. If the current element is equal to the target value, return the index of the current element.
5. Increment the index variable “i” by 1 after each iteration of the loop.
6. If the loop completes and the target value is not found, return -1 to indicate that the value is not present in the array.

'''
def sentinel_search(arr, n, key) -> int:
    last = arr[n-1] # take last item in arr in last var
    arr[n-1] = key # put key at last pos in arr

    # iterate over arr to find i where arr[i] = key
    i = 0
    while (arr[i]!= key):
        i+=1

    arr[n-1] = last # put last item back to end of array
    if ((i< n-1) or (arr[n-1]== key)):
        return key
    else:
        return -1
