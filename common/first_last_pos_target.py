def get_pos(target, arr)-> list:
    if len(arr) == 0 or target < arr[0] or target > arr[-1]:
        return [-1, -1]
    first = find_first(target, arr)
    last = find_last(target, arr)
    return [first, last]

def find_first(target, arr):
    if arr [0] == target:
        return 0
    start , end = 0, len(arr)-1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] == target and arr[mid-1] < target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid-1
    return -1


def find_last(target, arr):
    if arr[-1] == target:
        return len(arr)-1 
    start , end = 0, len(arr)-1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target and arr[mid+1] > target:
            return mid
        elif arr[mid]> target:
            end = mid -1
        else:
            start = mid +1
    return -1 
   


def main():
    arr = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
    print(get_pos(5, arr))

if __name__ == "__main__":
    main()