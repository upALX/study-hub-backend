# Read a given string, change the character at a given index and then print the modified string.

def mutate_string(string, position, character):
    
    new_string = string[:position] + character + string[position+1:] 
    
    return new_string

s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)