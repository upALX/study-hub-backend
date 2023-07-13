list_of_nums = [1,2,6,5,4,7,9,8]

for index, value in enumerate(list_of_nums):
    print(f'O index é {index} e o valor nessa posição é {value}')

print(list(enumerate(list_of_nums)))