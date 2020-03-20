/*
 * Complete the 'getUnallottedUsers' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. 2D_INTEGER_ARRAY bids
 *  2. INTEGER totalShares
 */

function sortOnMultipleParameter(arr) {
    const sortKey = (a, b) => {
        const [id1, count1, price1, time1] = a
        const [id2, count2, price2, time2] = b
        return price2 - price1 || time1 - time2 || id1 - id2;
    }
    arr.sort(sortKey)
}

function distribute(bids, shareCount) {
    const unallotedUsers = []
    for (let [id, count, price, time] of bids){
        if (shareCount <= 0) {
            unallotedUsers.push(id)
        }
        shareCount -= count
    }
    return unallotedUsers.sort()
}

function getUnallottedUsers(bids, totalShares) {
    sortOnMultipleParameter(bids)
    return distribute(bids, totalShares)
}