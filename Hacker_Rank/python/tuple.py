#Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .

n = int(input())
integer_list = map(int, (input().split()))

tuple_items = tuple(integer_list)
print(hash(tuple_items))
# print(tuple(hash(integer_list)))
        
