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

#74: Search a 2D Matrix
def searchMatrix(matrix, target):
    #Find the row that the element resides on. That is: the current column should be smaller then the item.
    row_found=False
    start=0
    end=len(matrix)-1
    while not row_found and start!=end:
        mid = (end+start)//2
        if matrix[mid][0] == target:
            return True
        elif matrix[mid][0] > target:
            end=mid
        else:
            if matrix[mid+1][0] > target:
                row_found=True
            else:
                start = mid+1
    if not row_found:
        if matrix[end][len(matrix[end])-1] < target:
            return False
        else:
            mid=end
    #Perform a binary search on the resulting array.
    arr = matrix[mid]
    start=0
    end = len(arr)-1
    while start<end:
        mid = ((end+start)//2)
        if target==arr[mid]:
            return True
        elif target < arr[mid]:
            end=mid-1
        else:
            start=mid+1
    if arr[start] == target:
        return True
    return False

matrix=[[-9,-8,-8],[-5,-3,-2],[0,2,2],[4,6,8]]
# print(searchMatrix(matrix,15))