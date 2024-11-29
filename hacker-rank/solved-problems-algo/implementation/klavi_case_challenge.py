# # Write a function that receives an input text and returns the number of appearances of the most
# frequent word. You can assume that the text only contains spaces and lower-case letters, and the words
# are separated by a single space.
phrase = input()

def get_most_words_appear_by_phrase(phrase: str) -> str: 

    counter_dict = {}

    for word in phrase.split():
        if word not in counter_dict:
            counter_dict[word] = 0
        counter_dict[word] += 1

    all_values_from_counter_dict_list = [value for value in counter_dict.values()]
    
    average_of_values = sum(all_values_from_counter_dict_list) / len(all_values_from_counter_dict_list)

    print(f'The average of appears is: {average_of_values:.2f}')

    # most_value_appears = sum(counter_dict.values())

    # print(most_value_appears)

    # more_words_appear_list = [word for word, sum_appears in counter_dict.items() if sum_appears == most_value_appears]    


    # if len(more_words_appear_list) == 1: 
    #     return f'The word {more_words_appear_list[0]} appears {most_value_appears} times in the input text'
    # else:
    #     return f'Both the words {' and '.join(more_words_appear_list)} appear {most_value_appears} times in the input text'

#because a function need return something
words_counted = get_most_words_appear_by_phrase(phrase=phrase)

print(words_counted)

# from collections import Counter

# def count_words_by_phrase_one(phrase_list: list) -> str:
#     counter_dict = Counter(phrase_list)

#     max_value = max(counter_dict.values())

#     words_more_appear = [word for word, counter_value  in counter_dict.items() if counter_value == max_value]    

#     return f'The word {words_more_appear[0]} appears {max_value} times in the input text' if len(words_more_appear) == 1 else f'Both the words {' and '.join(words_more_appear)} appear {max_value} times in the input text'
