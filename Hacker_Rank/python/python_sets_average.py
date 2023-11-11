# A set is an unordered collection of elements without duplicate entries.
# When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

def average(array):
    distinct_heights_set = set(array)
    
    average_distinct_heights = sum(distinct_heights_set) / len(distinct_heights_set)
    
    average_distinct_heights_rounded = f'{average_distinct_heights:.3f}'
    
    return average_distinct_heights_rounded

n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)