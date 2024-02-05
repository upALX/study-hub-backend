def utopianTree(cycles) -> None:
    # spring double, summer +1 meter
    # each year the three has 2 cycles
    # how long is the three after N cycles
    
    three_length = 0
    station = 'P'
    
    for cycle in range(cycles + 1):
        # print(f'The cycle is {cycle}')
        # if cycle == 0:
        #     three_length += 1
        #     station = 'P'
        #     print(f'Three length is {three_length} and station is {station}')
        # print(f'Cycle number {cycle}')
        if cycle % 2 == 0:
            three_length += 1
            station = 'P'
            # print(f'Three length is {three_length} and station is {station}')
        elif cycle < 3 and cycle % 2 != 0:
            three_length += three_length * three_length 
            station = 'V'
            # print(f'Three length is {three_length} and station is {station}')
        else:
            three_length += (three_length * 2) - three_length 
            station = 'V'
            # print(f'Three length is {three_length} and station is {station}')
            
            
    return three_length

t = int(input().strip())

for t_itr in range(t):
    n = int(input().strip())

    result = utopianTree(n)

