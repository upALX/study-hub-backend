#You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.). The center of the rangoli has the first alphabet letter a, and the boundary has the  alphabet letter (in alphabetical order).

def print_rangoli(size):
    # verify if size is > 0 and < 27
    if size > 0 and size < 27:
        for i in range(n-1,-1,-1):
            for j in range(i):
                print(end="--")
            for j in range(n-1,i,-1):
                print(chr(j+97),end="-")
            for j in range(i,n):
                if j != n-1:
                    print(chr(j+97),end="-")
                else:
                    print(chr(j+97),end="")
            for j in range(2*i):
                print(end="-")
            print()
        for i in range(1,n):
            for j in range(i):
                print(end="--")
            for j in range(n-1,i,-1):
                print(chr(j+97),end="-")
            for j in range(i,n):
                if j != n-1:
                    print(chr(j+97),end="-")
                else:
                    print(chr(j+97),end="")
            for j in range(2*i):
                print(end="-")
            print()

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)