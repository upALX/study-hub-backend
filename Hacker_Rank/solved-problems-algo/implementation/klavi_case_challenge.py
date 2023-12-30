# # Write a function that receives an input text and returns the number of appearances of the most
# frequent word. You can assume that the text only contains spaces and lower-case letters, and the words
# are separated by a single space.

phrase = 'quero comer milho eu nao quero comer batata eu nao quero comer coxinha'.split()

def count_words_by_phrase(phrase_list: list) -> str: 

    counter_dict = {}

    for word in phrase_list:
        if word not in counter_dict:
            counter_dict[word] = 0
        counter_dict[word] += 1

    max_value = max(counter_dict.values())

    words_more_appear = [word for word, counter_value  in counter_dict.items() if counter_value == max_value]    

    if len(words_more_appear) == 1: 
        return f'The word {words_more_appear[0]} appears {max_value} times in the input text'
    elif len(words_more_appear) > 1:
        return f'Both the words {' and '.join(words_more_appear)} appear {max_value} times in the input text'
    else:
        return f'There is no word appear more'

#because a function need return something
words_counted = count_words_by_phrase(phrase_list=phrase)

print(words_counted)