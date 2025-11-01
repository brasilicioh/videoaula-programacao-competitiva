# Feito por Kaio Henrique

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        printed = False

        for i in range(len(nums)):
            for e in range(len(nums)):
                if i != e and nums[i] + nums[e] == target and not printed:
                    return[i, e]
                    printed = True
                else:
                    continue

        return []

# Código testado e aprovado no LeetCode
# Runtime: 4069ms
# Memory Usage: 18.6MB

# Link do problema: https://leetcode.com/problems/two-sum/