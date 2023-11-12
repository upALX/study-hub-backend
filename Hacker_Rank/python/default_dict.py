# In this challenge, you will be given  integers,  and . There are  words, which might repeat, in word group . There are  words belonging to word group . For each  words, check whether the word has appeared in group  or not. Print the indices of each occurrence of  in group . If it does not appear, print .

# GET N AND M

# from collections import defaultdict

# lines_A_B = list(map(int, input().split())) 

# print(type(lines_A_B[0]))
# print(type(lines_A_B[1]))

# dict_with_values = defaultdict(list)

# dict_with_values['A'] = lines_A_B[0]
# dict_with_values['B'] = lines_A_B[1]

# print(dict_with_values)

# # Get the letter on group A

# for _ in range(dict_with_values['A']):
#     value = input()

#     dict_with_values['A.a'].append(value)

# # Get the letters of group B
# for _ in range(dict_with_values['B']):
#     value = input()
#     dict_with_values['B.b'].append(value)

# # Verify if B appear on A. If the B is on A, print the indice, if not print -1

# for index, value in enumerate(dict_with_values['B.b']):

#     list_values = []
#     print('LIST VALUES', list_values, 'index: ', index)
#     list_not_values = []
#     print('LIST NOT VALUES', list_not_values, 'index: ', index)

#     #IF A group contain the item of B, print the index
#     if value in dict_with_values['A.a']:
#         value_to_append = index + 1
#         dict_with_values['A.a.A'].append(str(index))
#         print('Value founded: ', value)
#     else:
#         dict_with_values['B.b.B'].append('-1')
#         print('Value not founded: ', value)

#     print(len(dict_with_values['B.b']), 'is', index + 1)

#     # All that appers on B must be printed

#     if index + 1 == len(dict_with_values['B.b']):
#         print('ON LIST VALUES, THE VALUES IS: ', dict_with_values['A.a.A'])
#         print(' '.join(dict_with_values['A.a.A'])) 

#         if len(dict_with_values['B.b.B']) != 0: 
#             print(' '.join(dict_with_values['B.b.B']))


# Input the integers n, m, and r
n, m, r = map(int, input().split())

# Input the words for group A
group_a = [input().strip() for _ in range(n)]

# Input the words for group B
group_b = [input().strip() for _ in range(m)]

# Iterate through words in group B
for word_b in group_b:
    indices = [str(i + 1) for i, word_a in enumerate(group_a) if word_a == word_b]

    if indices:
        print(" ".join(indices))
    else:
        print("-1")