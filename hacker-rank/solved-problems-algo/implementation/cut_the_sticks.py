# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# each iteration determine shortest stick, select it and cut this length of longest sticks. After that, discart the rest of pieces short stick.
    
#  When all the remaining sticks are the same length, they cannot be shortened so discard them.

#print the number of sticks that are left before each iteration until there are none left.

def cutTheSticks(arr):
    
    list_values_counter = []
    
    new_list = []
    
    while True:
        counter_stick_cut_list = 0
                
        # print('ARRAY: ', arr)
        #get min of arr
        new_list = arr.copy()
       
        min_value = min(item for item in new_list if item > 0)

        print('MIN VALUE: ', min_value)
        # remove the min of all values in arr
        for item in new_list:

            if item > 0:
                # print('INITIAL ITEM: ', item)
                arr.remove(item)
                item = (item - min_value)
                # print('ITEM: ', item)
                arr.append(item)
                # print('ARRAY NOW IS: ', arr)
                counter_stick_cut_list += 1

        print(counter_stick_cut_list)
        list_values_counter.append(counter_stick_cut_list)
        
        if all(element <= 0 for element in arr):
            print(arr)
            break
                
    return list_values_counter

n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

result = cutTheSticks(arr)

print(result)

# while True: 
#         counter_stick_cut_list = 0
                
#         print('ARRAY: ', arr)
#         #get min of arr
        
        
#         new_list = arr.copy()
        
#         non_zero_values_arr = filter(lambda x: x != 0, new_list)
                
#         min_value = min(non_zero_values_arr)
#         # remove the min of all values in arr
#         for item in new_list:
#             if item > 0:
        
#                 print('MIN VALUE: ', min_value)
#                 print('INITIAL ITEM: ', item)
#                 arr.remove(item)
#                 item = (item - min_value)
#                 print('ITEM: ', item)
#                 arr.append(item)
#                 print('ARRAY NOW IS: ', arr)
#                 counter_stick_cut_list += 1
        
#         # new_list = arr
        
#         print(counter_stick_cut_list)
#         list_values_counter.append(counter_stick_cut_list)
        
#         if all(element <= 0 for element in arr): 
#             break
                
#     return list_values_counter