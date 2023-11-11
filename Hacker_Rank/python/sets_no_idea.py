

# There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. You like all the integers in set  and dislike all the integers in set . Your initial happiness is . For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

# Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.

def calculate_happiness(array, set_a, set_b):
    happiness = 0

    for num in array:
        if num in set_a:
            happiness += 1
        elif num in set_b:
            happiness -= 1

    return happiness

n, m = map(int, input().split())
array = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

result = calculate_happiness(array, set_a, set_b)

print(result)