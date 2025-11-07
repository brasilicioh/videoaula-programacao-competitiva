// Feito por Guilherme Aleixo

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        use std::collections::HashMap;

        let mut map = HashMap::new();

        for (i, &num) in nums.iter().enumerate() {
            let complement = target - num;
            if let Some(&index) = map.get(&complement) {
                return vec![index as i32, i as i32];
            }
            map.insert(num, i);
        }

        vec![]
    }
};

// Código testado e aprovado no LeetCode
// Runtime: 0s
// Memory Usage: 2.68MB

// Link do problema: https://leetcode.com/problems/two-sum/