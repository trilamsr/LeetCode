const matrix = [
    [1,1,1,1,1,1,1],
    [1,1,1,1,0,0,0],
    [1,1,1,1,0,0,0],
    [1,1,1,1,0,0,0],
    [1,1,1,1,0,0,0],
    [1,1,1,1,1,1,1],
];

function largestMatrix (arr) {
    const [row, col] = [arr.length, arr[0].length];
    const table = new Array(row).fill(null);
		for (let i in table) {
			table[i] = new Array(col).fill(0)
		}
		let ret = 0;
		for (let i in arr) {
			for (let j in arr[i]) {
				if (arr[i][j] === 0) continue;
				const top = (i > 0) ? table[i-1][j] : 0;
				const topLeft = (j > 0 && i > 0) ? table[i-1][j-1] : 0;
				const left = (j > 0) ? table[i][j-1] : 0;
				table[i][j] = 1 + Math.min(left, topLeft, top);
				ret = Math.max(ret, table[i][j]);
			}
		}
		console.log(table)
		return ret;
}

console.log(largestMatrix(matrix));