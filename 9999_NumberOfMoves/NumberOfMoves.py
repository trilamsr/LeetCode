function inbound(i, j, n) {
    const row = 0 <= i && i < n
    const col = 0 <= j && j < n
    return row && col
}

function getCellID(i, j, size) {
    let id = (i * size) + j
    return id
}

const possibleMoves = [
    [1, 2],
    [2, 1],
    [-1, 2],
    [-2, 1],
    [1, -2],
    [2, -1],
    [-2, -1],
    [-1, -2],
]

function* validNeighbor(i, j, visited, size) {
    for (let [di, dj] of possibleMoves) {
        let [y, x] = [i + di, j + dj];
        if (!inbound(y, x, size)) continue;
        let cellID = getCellID(y, x, size)
        if (visited.has(cellID)) continue;
        yield [y, x]
    }
}

function minMoves(n, startRow, startCol, endRow, endCol) {
    let level = 0;
    const visited = new Set();
    const queue = [
        [startRow, startCol]
    ];
    while (queue) {
        let levelCount = queue.length;
        for (let count = 0; count < levelCount; count++) {
            let [i, j] = queue.shift()
            let cellID = getCellID(i, j, n)
            if (visited.has(cellID)) continue;
            visited.add(cellID)
            if (i === endRow && j === endCol) return level;
            for (let neigh of validNeighbor(i, j, visited, n)) {
                queue.push(neigh)
            }
        }
        level++
    }
    return -1
}