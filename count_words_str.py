def count_words(sentence):
    words = sentence.split()  # Split the sentence into words
    return len(words)  # Return the count of words

# Example usage:
sentence = "Hello, how are you?"
print("Number of words in the sentence:", count_words(sentence))

