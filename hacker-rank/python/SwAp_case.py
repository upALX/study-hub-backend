# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(full_phrase):
    list_of_words = []
    for word in full_phrase:
        for letter in word:
            if letter.islower():

                new_word = letter.upper()
                list_of_words.append(new_word)
            elif letter == " ":
                list_of_words.append(letter)
            else:
                 new_word = letter.lower()
                 list_of_words.append(new_word)

    print(''.join(list_of_words))
        
s = input()
result = swap_case(s)