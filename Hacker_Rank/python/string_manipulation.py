#You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

def split_and_join(line):
    
    joined_string = line.replace(" ", "-")
    
    return joined_string

line = input()
result = split_and_join(line)
print(result)