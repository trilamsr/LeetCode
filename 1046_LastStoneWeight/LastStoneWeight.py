class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones: return 0
        stones.sort()
        while stones:
            rockA = stones.pop()
            if not stones: return rockA
            rockB = stones.pop()
            rock = abs(rockA-rockB)
            if rock:
                stones.append(rock)
            if stones:
                stones.sort()
            else:
                return 0





# def swap (arr,a,b):
#     arr[a], arr[b] = arr[b], arr[a]
    
# def max_heapify_down(ind, arr):
#     left = (ind*2)+1 if (ind*2)+1 < len(arr) else 0 
#     right = (ind*2)+2 if (ind*2)+2 < len(arr) else 0
#     max_index = ind
#     if left and arr[left] > arr[max_index]:
#         max_index = left
#     if right and arr[right] > arr[max_index]:
#         max_index = right 
#     if max_index != ind:
#         swap(arr, max_index, ind)
#         max_heapify_down(max_index, arr)

# def max_heapify_up(ind, arr):
#     parent = (ind-1)//2
#     if arr[ind] > arr[parent]:
#         swap(arr, ind, parent)
#         max_heapify_up(parent, arr)

# def pop(arr):
#     swap(arr, 0, len(arr)-1)
#     ret = arr.pop()
#     max_heapify_down(0, arr)
#     return ret

# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         if not stones: return 0
#         for i in range(len(stones)//2, -1, -1):
#             max_heapify_down(i, stones)
#         print("HEAP")
#         while len(stones) > 1:
#             print(stones)
#             first = pop(stones)
#             second = pop(stones)
#             print(f"FIRST: {first}")
#             print(f"FIRST: {second}")
#             rock = abs(first-second)
#             if rock: stones.append(rock)
#             if stones: max_heapify_up(len(stones)-1, stones)
#         return stones[0] if stones else 0