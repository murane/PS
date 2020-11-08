import math
def solve():
    n, m, k = list(map(int, input().split(" ")))
    arr = list(map(int, input().split(" ")))
    query = list(map(int, input().split(" ")))
    indexes = {}
    values = {}
 
    for i in range(n):
        indexes[arr[i]] = i
        values[i] = arr[i]
 
    moves = 0
    for i in query:
        moves += math.ceil(indexes[i] // k) + 1
 
        if indexes[i] == 0:
            continue
 
        # Swap indexes
        current_index = indexes[i]
        prev_value = values[current_index - 1]
        tmp = current_index
        indexes[i] = current_index - 1
        indexes[prev_value] = current_index
 
        # Swap value order
        values[current_index - 1] = i
        values[current_index] = prev_value
 
    print(moves)
 
solve()
