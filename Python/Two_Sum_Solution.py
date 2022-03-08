#!/usr/bin/env python
# coding=utf-8
# @author qujianning
# @date 2022-03-08 第1天
# @input: nums = [2, 3, 4, 5]  target = 9
# @brief: 给定一个数组和一个目标和，从数组中找两个数字相加等于目标和，输出这两个数字的下标
# @output: [2, 3]

def Two_Sum_Solution_1(nums, target):
    '''
        方法1: 使用暴力的方法，直接遍历所有情况
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

if __name__ == "__main__":
    nums = [2, 3, 4, 5]
    target = 9
    print(Two_Sum_Solution_1(nums, target))