"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Eg. 1

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


Eg. 2
Input: nums = [3,2,4], target = 6
Output: [1,2]

Eg. 3
Input: nums = [3,3], target = 6
Output: [0,1]

"""

from typing import List
import logging

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print(nums)
        sorted_nums = nums
        sorted_nums.sort()
        # logging.info(sorted_nums)
        print(f'sorted nums: {sorted_nums}')
        return sorted_nums