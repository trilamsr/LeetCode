/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */

function merge (l1, l2){
    let ret = new ListNode("dummy");
    let cur = ret;
    while (l1 && l2){
        if (l1.val < l2.val) {
            [cur.next, l1] = [l1, l1.next];
        } else {
            [cur.next, l2] = [l2, l2.next];
        }
        cur = cur.next
    }
    cur.next = l1 || l2;
    return ret.next
}

var mergeKLists = function(lists) {
    if (lists.length === 0) return null;
    for (let k = 1; k < lists.length; k*=2) {
        for (let i = 0; i < lists.length; i += 2*k) {
            lists[i] = merge(lists[i], lists[i+k]);
        }
    }
    return lists[0]
};
























