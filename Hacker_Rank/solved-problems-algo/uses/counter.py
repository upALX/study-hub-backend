from collections import Counter


# Use on files

def count_letters_by_file(filename) -> Counter:

    letter_counter = Counter()

    with filename as file:
        for line in file:
            line_letters = [letter for letter in line.lower() if letter.isalpha()]

            letter_counter.update(Counter(line_letters))
    
    return letter_counter
