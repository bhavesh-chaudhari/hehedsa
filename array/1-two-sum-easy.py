# https://leetcode.com/problems/two-sum/
from typing import List

def twoSum(nums: List[int], target: int):
    res = {}
    for i, n in enumerate(nums):
        j = target - n
        if j in res:
            return [res[j], i]
        else:
            res[n] = i

if __name__ == "__main__":
    result = twoSum([3, 3], 6)
    print(result)