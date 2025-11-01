// Feito por Brasilicio Henrique

#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> view;
        int complement, length = nums.size();

        for (int i = 0; i < length; i++) {
            complement = target - nums[i];
            if (view.find(complement) != view.end()) {
                return {view[complement], i};
            }
            view[nums[i]] = i;
        }

        return {};
    }
};

// Código testado e aprovado no LeetCode
// Runtime: 0ms
// Memory Usage: 14.8MB

// Link do problema: https://leetcode.com/problems/two-sum/