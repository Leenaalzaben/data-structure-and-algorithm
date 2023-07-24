import string

def repeated_word(s):
    # Step 1: Remove punctuation from the input string
    translator = str.maketrans('', '', string.punctuation)
    s = s.translate(translator)

    # Step 2: Split the input string into words
    words = s.split()

    # Step 3: Create a hashmap to store word frequencies
    word_freq = {}

    # Step 4: Traverse through each word and update the hashmap
    for word in words:
        # Convert the word to lowercase to handle case-insensitivity
        word = word.lower()

        # Increment the frequency count in the hashmap
        word_freq[word] = word_freq.get(word, 0) + 1

        # Step 5: Check if the current word is repeated
        if word_freq[word] > 1:
            return word

    # If no repeated word found, return None
    return None


input_string = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
result = repeated_word(input_string)

print("Input String:", input_string)
print("First Repeated Word:", result)
