# Given an array of integers and a positive integer K, DETERMINE THE NUMBER OF (I,J) PAIR WHERE I < J AND AR[I] + AR[J] is divisible by K.

from itertools import permutations

def divisibleSumPairs(n, k, ar):
    # Write your code here
    list_with_pairs = []

    pairs = [(i, j)for i in ar for j in ar if i < j]

    print('PAIRS', pairs)
    
    for pair in pairs:
        if sum(pair) % k == 0:
            list_with_pairs.append(pair)
            print('PAIR ADDED: ', pair)

    print('FINAL LIST PAIRS', list_with_pairs)

    return list_with_pairs.__len__()

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

ar = list(map(int, input().rstrip().split()))

result = divisibleSumPairs(n, k, ar)

print(result)