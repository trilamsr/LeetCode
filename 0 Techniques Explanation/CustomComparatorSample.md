<!-- java or javascript -->
function key(A, B) {
    if (A.isPrime != B.isPrime) {
        return (1 ^ A.isPrime) - (1 ^ B.isPrime);
    } else if (A.rest != B.rest) {
        return (A.rest < B.rest) ? 1 : -1;
    } else {
        return A.id - B.id;
    }
}


a-b imply a < b imply a-b < 0 - Ascending

arr.sort((a,b)=> {
    return a-b
})


<!-- Python -->

class Item:
    def __init__(self, order):
        ords = order.split()
        self.order = order
        self.id = int(ords[0])
        self.is_prime = ords[1][0].isalpha()
        self.rest = ' '.join(ords[1:])
        self.key = (int(not self.is_prime), self.rest, self.id)

    def __lt__(self, other):
        return self.key < other.key

    def __str__(self):
        return self.order

def sort_amazon(orders):
    orders = [Item(item) for item in orders]
    orders.sort()
    ret = [str(item) for item in orders]
    return ret