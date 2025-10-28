def word_frequency(sentence):
    words = sentence.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

# Example
text = "Python is fun and learning Python is easy"
print(word_frequency(text))
