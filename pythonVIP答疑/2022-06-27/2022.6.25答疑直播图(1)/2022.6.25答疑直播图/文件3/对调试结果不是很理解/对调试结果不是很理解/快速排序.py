# _*_ coding: utf-8 _*_
# _*_操作人 : 魏杰阳 _*_

def partition(nums,left,right):
    pivot = nums[left]
    while left < right:
        while left < right and nums[right] > pivot:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] < pivot:
            left += 1
        nums[right] = nums[left]
    nums[left] = pivot
    return left

def QuickSort(nums,left,right):
    if left >= right:
        return
    pivot_index = partition(nums,left,right)        #
    print("right:", right)
    print(nums,pivot_index)
    QuickSort(nums,left,pivot_index-1)
    print(pivot_index)
    QuickSort(nums,pivot_index+1,right)


test = [44, 12, 59, 36, 62, 43, 94, 7, 35, 52, 85]
QuickSort(test,0,len(test)-1)
print(test)

















