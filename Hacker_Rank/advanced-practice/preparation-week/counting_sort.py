def countingSort(arr):
    # Write your code here
    max_value = max(arr)

    # Create a counting array to store the count of each element
    count_array = [0] * (max_value + 1)

    # Count the occurrences of each element in the array
    for num in arr+1:
        count_array[num] += 1
        
    return count_array

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    print(' '.join(map(str, result)))
