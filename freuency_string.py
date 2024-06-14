#WRITE PYTHON PROGRAM TO COUNT THE FREQUENCY OF WORDS APPEARING IN A STRING

def frequency_words():
    input_str=input("enter the string")
    li=input_str.split()
    d={}
    for i in li:
        if i not in d.keys():
            d[i]=0
        d[i]=d[i]+1
    print(d)
frequency_words()

def count_words(sentence):
    words = sentence.split()  # Split the sentence into words
    return len(words)  # Return the count of words

# Example usage:
sentence = "Hello, how are you?"
print("Number of words in the sentence:", count_words(sentence))
