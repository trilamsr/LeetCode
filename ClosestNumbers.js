/* eslint-disable no-unused-vars */
function closestNumbers (numbers) {
	let sorted = numbers.sort((a, b) => a-b);
	let table = {};
	let minKey = Infinity;
	for (let i = 1; i < sorted.length; i++) {
		let diff = sorted[i] - sorted[i-1];
		if (!table[diff]) {
			table[diff] = [];
		}
		table[diff].push([sorted[i-1], sorted[i]])
		minKey = Math.min(diff, minKey)
	}
	return table[minKey]
}

function closestNumbersLong (numbers) {
  let sorted = quickSort (numbers);
	let difference = Infinity;
	let ret = [];
	for (let i = 1; i < sorted.length; i++){
		if (sorted[i-1] === sorted[i]) {
      continue;
		} else {
      let curDif = sorted[i] - sorted[i-1];
			if (curDif > difference) {
        continue;
			} else if (curDif === difference) {
        ret.push([sorted[i-1], sorted[i]])
			} else {
        difference = curDif;
				ret = [];
				ret.push([sorted[i-1], sorted[i]])
			}
		}
	}
	return ret;
}

function swap(array, x, y) {
  [array[y], array[x]] = [array[x], array[y]];
}

function partition(array, lo, hi) {
  let position = lo + Math.floor((hi - lo + 1) * Math.random());
  let pivot = array[position];
  for (let i = lo; i <= hi; i++) {
    if (array[i] < pivot) {
      swap(array, i, lo++);
    } else if (array[i] > pivot) {
      swap(array, i--, hi--);
    }
  }
  return [lo, hi];
}

function quickSort(array) {
  qSort(array, 0, array.length - 1);
  return array;
}

function qSort(array, lo, hi) {
  if (lo >= hi) return;
  let [pLo, pHi] = partition(array, lo, hi);
  qSort(array, lo, pLo - 1);
  qSort(array, pHi + 1, hi);
}
