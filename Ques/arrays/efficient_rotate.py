
def rotate(nums, k):
    k= k% len(nums)
    start = len(nums) -k
    end = len(nums) -1
    while start< end:
        nums[start], nums[end] = nums[end], nums[start]
        start+=1
        end-=1  

    start = 0
    end = len(nums)-k-1
    while start < end:
        nums[start] , nums[end]= nums[end], nums[start]
        start +=1
        end-=1

    start = 0
    end = len(nums) -1
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start +=1
        end -=1
    return nums

def main():
    nums = [1,2,3,4,5,6,7]
    k = 5
    print(rotate(nums, k))


if __name__ == "__main__":
    main()
 

        
        