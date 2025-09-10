# 全世界最帅的帅哥
# coding=utf-8

def merge(left,right):
    # 最终返回一个合并好的有序的数组
    # 定义两个变量，分别代表当前left与right的未添加进有序数组的第一个元素
    left_idx,right_idx = 0, 0
    res = []  # 有序数组
    while left_idx < len(left) and right_idx < len(right):
        # 实现有序
        if left[left_idx] < right[right_idx]:
            res.append(left[left_idx])
            left_idx += 1
        else:
            res.append(right[right_idx])
            right_idx += 1
    res += right[right_idx:] #把剩余的未添加的元素全部添加到有序数组后面
    res += left[left_idx:] #left，right本身是一个有序数组
    return res

def mergeSort(nums):
    # 分
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    print(nums[:mid],nums[mid:])   # 第一次切片
    # 左边
    left = mergeSort(nums[:mid])
    # 右边
    right = mergeSort(nums[mid:])
    # 合
    return merge(left,right)

test = [1,4,2,7,23,9,41,24,52,65]
test = mergeSort(test)
print(test)