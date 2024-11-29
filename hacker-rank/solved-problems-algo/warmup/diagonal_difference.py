# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

def diagonalDifference(arr) -> int:
    counter = 0
    reversed_list = reversed(arr)
    list_left = []
    list_right = []
    for index, item in enumerate(arr):
        # if len(item) == len(item[index + 1]):
        for index, value in enumerate(item):
            print('value', value)
            if index == counter:
                list_left.append(value)
                counter += 1
                break

    counter = 0
    
    for index, item in enumerate(reversed_list):
        # if len(item) == len(item[index + 1]):

        for index, value in enumerate(item):
            print('value', value)
            if index == counter:
                list_right.append(value)
                counter += 1
                break

    result_not_abs = sum(list_left) - sum(list_right)

    print(abs(result_not_abs))

    return abs(result_not_abs)

# first line contain a single integer
n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)

print(result)