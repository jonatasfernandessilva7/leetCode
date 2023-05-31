/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let map = new Map();
    for (let i = 0; i < nums.length; i++){
        var complementos  = target - nums[i];
        if (map.has(complementos)){
            return [i, map.get(complementos)];
        }
        map.set(nums[i], i)
    }
}