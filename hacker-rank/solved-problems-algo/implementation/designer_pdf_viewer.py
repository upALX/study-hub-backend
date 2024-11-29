#!/bin/python3

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    alphabet_mapping = {chr(ord('a') + i): h[i] for i in range(26)}
    word_dict = {letter: 0 for letter in word}
    
    word_mapped = {letter: value for letter, value in alphabet_mapping.items() if letter in word_dict}
    
    print(alphabet_mapping)
    
    width_caracter = 1
    
    print(word_mapped)
    # determine the area of the retangle mm2 
    # all letters are 1mm wide
    tallest_letter = max(word_mapped.values())
    height_cover_word = tallest_letter * width_caracter * len(word)

    return height_cover_word


h = list(map(int, input().rstrip().split()))

word = input()

result = designerPdfViewer(h, word)

print(result)