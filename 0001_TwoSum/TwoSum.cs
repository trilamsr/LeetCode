
public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int,int> mem = new Dictionary<int, int>();
			foreach (var x in nums.Select((val, ind) => new {val, ind})) {
				if (mem.ContainsKey(x.val)) {
					return new int[]{mem[x.val], x.ind};
				}
				mem[target-x.val] = mem.ContainsKey(target-x.val) ? mem[target-x.val] : x.ind;
			}
			return new int[] {0,0};
    }
}