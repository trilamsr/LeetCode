/* eslint-disable no-console */
/* eslint-disable no-unused-vars */
//Get all the possible answers
function maxStep (n, k) {
	let ret = [];
	function recurse(maxAct, notThis, curAction, curStep, ret) {
		if (curAction <= maxAct && curStep !== notThis) {
			recurse (maxAct, notThis, curAction + 1, curStep + curAction, ret)
			recurse (maxAct, notThis, curAction + 1, curStep, ret)
		} else {
			if (curStep !== notThis) {
				ret.push(curStep)
			}
		}
	}
	recurse(n, k, 1, 0, ret);
	return Math.max(...ret)
}

//Get the 1 answer
function betterMaxStep (n, k) {
	function recurse (n,k, pos, step) {
	if (step === n + 1) return pos;
	if (pos + step === k) {
		return recurse (n, k, pos+ step -1, step+1)
	}
	return recurse (n, k, pos+step, step+1)
	}
	return recurse(n, k, 0, 1)
}
// The one and only
function maxStep3(n, k) {
	let pos = 0;
	for (let jump = 1; jump <= n; ++jump) {
		const backpedal = (pos + jump == k) ? -1 : 0;
		pos += jump + backpedal;
	}
	return pos;
}

console.log('expect 5, avoid 3')

console.time('solution 1Test1')
console.log(maxStep(3,3))
console.timeEnd('solution 1Test1')

console.time('solution 2 Test 1')
console.log(betterMaxStep(3,3))
console.timeEnd('solution 2 Test 1')

console.log('--------------------')

console.log('expect 2, avoid 1')

console.time('solution 1 Test 2')
console.log(maxStep(2,1))
console.timeEnd('solution 1 Test 2')

console.time('solution 2 Test 2')
console.log(betterMaxStep(2,1))
console.timeEnd('solution 2 Test 2')
console.log('--------------------')

console.log('expect 3, avoid 2')

console.time('solution 1 Test 3')
console.log(maxStep(2,2))
console.timeEnd('solution 1 Test 3')

console.time('solution 2 Test 3')
console.log(betterMaxStep(2,2))
console.timeEnd('solution 2 Test 3')

console.log('--------------------')
