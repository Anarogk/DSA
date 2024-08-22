def insertion_sort(arr):
    # First for loop is for iterating from 1 to len(arr)
    for i in range(1, len(arr)):
        # we set curr to arr[i]
        curr = arr[i]
        # we set j to be one less than i
        j = i - 1
        # then when j is natural no. and curr is smaller than arr[j]
        while (j > -1 and curr < arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = curr
    return arr


def main():
    arr = [1, 4, 5, 6, 9, 10, 2, 6, 7, 3, 8, 4]
    print(insertion_sort(arr))


if __name__ == "__main__":
    main()
