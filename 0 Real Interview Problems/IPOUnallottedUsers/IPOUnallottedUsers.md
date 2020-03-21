# 8. Initial Public Offering (Braze Version)

A company registers an IPO on a website sellshares.com. All the shares on this website are available for bidding for a particular time frame called the bidding window. 
At the end of the bidding window an auction logic is used to decide how many of the available shares go to which bidder until all the shares that are available have been allotted, or all the bidders have received the shares they bid for, whichever comes earlier.

The bids arrive from the users in the form of <user Id, number of shares, bidding price, timestamp> until the bidding window is closed.

The auction logic assigns shares to the bidders as follows:

1. The bidder with the highest price gets the number of shares they bid for
2. If multiple bidders have bid at the same price, the bidders are assigned shares in the order in which they placed their bids (earliest bids first).

List the user Id’s of all users who did not get even one share after the shares have been allocated.

**For example:**

    Bids come in as bids = [[1, 5, 5, 0], [2, 7, 8, 1], [3, 7, 5, 1], [4, 10, 3, 3]]
    There are totalShares = 18 to allocate. 
    Output: [4]
    Explanation:
        The highest price bid is for user Id 2 for 7 shares at a price of 8, so that user gets 7 shares leaving 11 to allocate to lower prices. Users with Id's 1 and 3 each bid 5 for 5 and 7 shares, with bidder 1 having the earlier timestamp. Bidder 1 has the full allotment, bidder 3 has 2 more shares to buy and there is 1 share left to allocate. It goes to bidder 3 and all shares have been allotted. Bidder 4 is the only bidder who gets no shares.
    
## Function Description:

Complete the function getUnallottedUsers in the editor below. The function must return a list of integers, each an Id for those bidders who receive no shares, sorted ascending.
getUnallottedUsers has the following parameter(s):
    bids[bids[0],...bids[n-1]]: a 2D array of arrays of integers, Id, shares, price, timestamp
    totalShares: an integer, the total shares to allocateConstraints1 ≤ n < 1041 ≤ u, sc, bp, ts, totalShares < 10^8