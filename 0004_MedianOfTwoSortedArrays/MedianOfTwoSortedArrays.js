/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    if (nums1.length > nums2.length) {[nums1, nums2] = [nums2, nums1]}
    let [x,y] = [nums1.length, nums2.length]
    let [start, end] = [0, nums1.length]
    while (start <= end) {
        let parX = ~~((start+end)/2);
        let parY = ~~((x+y+1)/2) - parX;
        let leftMaxX = parX === 0 ? -Infinity : nums1[parX-1];
        let rightMinX = parX === x ?  Infinity : nums1[parX];
        let leftMaxY = parY === 0 ? -Infinity : nums2[parY-1];
        let rightMinY = parY === y ?  Infinity : nums2[parY];
        if (leftMaxX <= rightMinY && leftMaxY <= rightMinX) {
            if ((x+y)%2 === 0) {
                return (Math.max(leftMaxX,leftMaxY) + Math.min(rightMinX, rightMinY))/2;
            } else {
                return Math.max(leftMaxX, leftMaxY);
            }
        } else if (leftMaxX > rightMinY) {
            end = parX-1;
        } else {
            start = parX+1;
        }
    }
};