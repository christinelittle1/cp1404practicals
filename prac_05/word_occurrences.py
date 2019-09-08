word_occurrences = {}

text = input("Text: ")
words = text.split(" ")
words.sort()

for word in words:
    count = words.count(word)
    word_occurrences[word] = count

for word in word_occurrences:
    print("{}: {}".format(word, word_occurrences[word]))

