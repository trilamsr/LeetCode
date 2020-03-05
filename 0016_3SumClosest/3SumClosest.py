class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ret = math.inf
        for i in range(len(nums)-1):
            lo, hi = i+1, len(nums)-1
            while lo < hi:            
                total = nums[i]+nums[lo]+nums[hi]
                error = abs(target-total)
                if error < abs(target-ret):
                    ret = total
                if total == target: return total
                if total > target: hi -= 1
                if total < target: lo += 1
        return ret


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        error = math.inf
        total = math.inf
        for i, num in enumerate(nums):
            new_error, subsum = self.two_sums(nums, i+1, target-num)
            print(new_error, subsum, num)
            if new_error < error:
                total = num + subsum
                error = new_error
        return total
    
    def two_sums(self, nums, ind, target):
        error, total = math.inf, math.inf
        lo, hi = ind, len(nums)-1
        while lo < hi and error > 0:
            cur_total = nums[lo] + nums[hi]
            cur_error = abs(target-cur_total)
            if cur_error < error:
                error = cur_error
                total = cur_total
            if cur_total < target: lo += 1
            if cur_total > 0: hi -= 1
        return error, total
# ------------------------------------------