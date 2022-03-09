#!/usr/bin/env python
# coding=utf-8
# @author qujianning
# @date 2022-03-08 第1天
# @input: nums = [2, 3, 4, 5]  target = 9
# @brief: 给定一个数组和一个目标和，从数组中找两个数字相加等于目标和，输出这两个数字的下标
# @output: [2, 3]

def Two_Sum_Solution_1(nums, target):
    '''
        方法1: 使用暴力的方法，直接遍历所有情况，由于有两层for循环，因此时间复杂度为O(n²)
    '''
    ans = []
    nums_length = len(nums)
    for i in range(0, nums_length):
        for j in range((i+1), nums_length):
            if (nums[i] + nums[j]) == target:
                ans.append(i)
                ans.append(j)
                return ans
            else:
                continue

def Two_Sum_Solution_2(nums, target):
    '''
        方法2: 把数组里的值作为key，索引作为value存在map里，然后遍历数组，target和当前数字的差值如果在map的key中，就返回这个key的value
        这种方法，时间复杂度为O(n)，同时由于引入了map，所以空间复杂度为O(n)，和方法1相比，就是用空间换了时间
    '''
    kv_map = {}
    i = 0
    for num in nums:
        kv_map[num] = i
        i += 1
    for num in nums:
        sub = target - num
        if sub in kv_map and sub != num:
            return [kv_map[num],kv_map[sub]]

if __name__ == "__main__":
    nums = [2, 3, 4, 5]
    target = 9
    print(Two_Sum_Solution_1(nums, target))
    print(Two_Sum_Solution_2(nums, target))