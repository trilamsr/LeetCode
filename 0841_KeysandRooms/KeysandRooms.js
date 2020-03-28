var canVisitAllRooms = function(rooms) {
    const visited = new Set([0])
    const queue = [0]
    while (queue.length){
        let des = queue.pop()
        for (let key of rooms[des]) {
            if (visited.has(key)) continue
            visited.add(key)
            queue.push(key)
        }
    }
    return visited.size === rooms.length
};