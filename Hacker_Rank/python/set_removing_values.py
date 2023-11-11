# You have a non-empty set , and you have to execute  commands given in  lines.

# The commands will be pop, remove and discard.

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
s = set(map(int, input().split()))
num_commands = int(input())

for i in range(num_commands):
    command = input().split()
    print('COMMAND: ', command)
    if command[0] == "pop" and command.__len__() == 1:
        element = s.pop()
        print('IS POP remove: ', s)
    elif command[0] == "remove" and int(command[1]) in s:

        s.remove(int(command[1]))
        print('AFTER REMOVE: ', s)
    elif command[0] == "discard":
        s.discard(int(command[1]))

        print('AFTER DISCART: ', s)

print(s)
            
print(sum(s))
    