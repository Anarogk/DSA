def binary_search(arr, key):
    start , end = 0, len(arr)-1
    mid = start + end//2

    if key< mid:
        return binary_search_helper(arr, key, start, mid-1)
    elif key>mid:
        return binary_search_helper(arr, key, mid+1, end)
    
def binary_search_helper(arr,key,  start, end):
    mid = start + end//2

    if arr[mid] == key:
        return mid
    elif key > arr[mid]:
        return binary_search_helper(arr, key, mid+1, end)
    elif key < arr[mid]:
        return binary_search_helper(arr, key, start, mid-1)
    
def main():
    arr = [8,4,6,7,7,4,1,24,5,6,3,44]
    print(binary_search(arr,24))
