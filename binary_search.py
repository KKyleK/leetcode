#704: Binary search.
def search(nums, target):
    offset=0
    #Binary search: If my number is greater then half, search in greater half of the array.
    while len(nums) > 0:
        half = (len(nums))//2
        if target==nums[half]:
            return half+offset
        elif target > nums[half]:
            offset+=half+1
            nums = nums[half+1:]
        else:
            nums = nums[0:half]
    return -1

# nums=[-1,0,3,5,9,12]
# target=9
# print(search(nums,target))