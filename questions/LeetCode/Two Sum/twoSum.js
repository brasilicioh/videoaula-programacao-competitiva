// Feito por Brasilicio Henrique

var twoSum = function(nums, target) {
    const dict = new Map();
    let complemento;

    for (let i = 0; i < nums.length; i++) {
        complemento = target - nums[i];
        if (dict.has(complemento)) {
            return [dict.get(complemento), i];
        }
        dict.set(nums[i], i);
    }

    return [];
};

// Código testado e aprovado no LeetCode
// Runtime: 0s
// Memory Usage: 58.64MB

// Link do problema: https://leetcode.com/problems/two-sum/