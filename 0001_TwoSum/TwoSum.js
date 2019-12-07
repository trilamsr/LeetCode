var twoSum = function (nums, target) {
    const dict = {}
    for (let i in nums) {
        if (dict[nums[i]]) {
            return [dict[nums[i]], i]
        } else {
            dict[target - nums[i]] = i;
        }
    }
};

twoSum([2, 7, 11, 15], 9)