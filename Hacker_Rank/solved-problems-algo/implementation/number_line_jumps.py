def kangaroo(x1, v1, x2, v2):
    # Write your code here

    #x1 is start location of jumps

    #v1 is the lenght of each jump

    #x2 is start location of kangaroo 2 jumps

    #v2 is the lenght of each jump

    # find a form to set both kangoroos on the same position on show. If is possible, print YES, if not print NO

   pass


first_multiple_input = input().rstrip().split()

x1 = int(first_multiple_input[0])

v1 = int(first_multiple_input[1])

x2 = int(first_multiple_input[2])

v2 = int(first_multiple_input[3])

result = kangaroo(x1, v1, x2, v2)
