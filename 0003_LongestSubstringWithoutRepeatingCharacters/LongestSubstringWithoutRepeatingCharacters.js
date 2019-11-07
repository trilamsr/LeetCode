function lengthOfLongestSubstring (str) {
	let mem = new Set();
	let ret = 0;
	let [left, right] = [0,0]
	while ( left < str.length && right < str.length) {
		if (!mem.has(str[right])) {
			mem.add(str[right]);
			right++
		} else {
			mem.delete(str[left])
			left++
		}
		ret = Math.max(ret, mem.size)
	}
	return ret
}