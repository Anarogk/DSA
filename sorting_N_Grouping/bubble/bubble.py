def bubble_sort(arr):
    # first loop to iterate as many times as many items are in arr
    for i in range(len(arr)):
        # Second for loop to iterate through arr for items 1 lower than ith iteration as biggest already get settled from last
        for j in range(len(arr) - i - 1):
            # if one on left is greater than one on right shift them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def main():
    arr = [1, 4, 5, 6, 9, 10, 2, 6, 7, 3, 8, 4]
    print(bubble_sort(arr))


if __name__ == "__main__":
    main()
