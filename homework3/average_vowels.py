# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()


# Hint: You can use .isalpha() to check if a character is a letter.

def counting_vowels_and_consonants(string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in string:
        if char.isalpha():  
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return (vowel_count, consonant_count)

print(counting_vowels_and_consonants("The universe is infinite"))

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 

def average_vowels_and_consonants(paragraph):
    import re
    sentences = re.split(r'[.!?]+', paragraph)
    sentences = [s.strip() for s in sentences if s.strip()]
    total_vowels = 0
    total_consonants = 0
    for sentence in sentences:
        vowels, consonants = counting_vowels_and_consonants(sentence)
        total_vowels += vowels
        total_consonants += consonants
    num_sentences = len(sentences)
    avg_vowels = total_vowels / num_sentences if num_sentences > 0 else 0
    avg_consonants = total_consonants / num_sentences if num_sentences > 0 else 0
    return (num_sentences, avg_vowels, avg_consonants)

result = average_vowels_and_consonants(paragraph)

print(f"Number of sentences: {result[0]}")
print(f"Average vowels per sentence: {result[1]:.2f}")
print(f"Average consonants per sentence: {result[2]:.2f}")