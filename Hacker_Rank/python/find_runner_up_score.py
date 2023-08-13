n = int(input())
arr = map(int, input().split())
    
sorted_arr = sorted(arr)
    
if sorted_arr[-1] != sorted_arr[-2]:
    print(sorted_arr[-2]) 
else:
    last_item = [item for item in sorted_arr if item != sorted_arr[-1]]
    print(last_item)
    print(last_item[-1])
    