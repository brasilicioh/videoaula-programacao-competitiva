// Feito por Guilherme Aleixo

#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int* result = (int*)malloc(2 * sizeof(int));
    
    *returnSize = 2;

    for(int i = 1; i < numsSize; i++) {
        for(int j = i; j < numsSize; j++) {
            if(nums[j] + nums[j - i] == target) {
                result[0] = j - i;
                result[1] = j;
                return result;
            }
        }
    }

    return NULL;
};

// Código testado e aprovado no LeetCode
// Runtime: 0s
// Memory Usage: 8.51MB

// Link do problema: https://leetcode.com/problems/two-sum/