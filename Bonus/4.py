# Write your solution for algorithm 4 below
def sort_words_alphabetically(input_str):
    # Split the input string into words
    words = input_str.split()

    # Sort the words case-insensitively using a custom key
    sorted_words = sorted(words, key=lambda word: word.lower())

    return sorted_words

# Example usage:
input_str = 'I love software engineering'
sorted_words = sort_words_alphabetically(input_str)
print(sorted_words)
