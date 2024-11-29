# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be X. ( is an odd natural number, and  is  times .)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.

# Input Format

# A single line containing the space separated values of  and .

# Constraints


def print_door_mat(rows, cols):
    pattern = [('.|.' * (2 * i + 1)).center(cols, '-') for i in range(rows // 2)]
    welcome_line = 'WELCOME'.center(cols, '-')
    door_mat = pattern + [welcome_line] + pattern[::-1]

    for line in door_mat:
        print(line)

N = list(map(int, input().split()))

print_door_mat(N[0], N[1])
        