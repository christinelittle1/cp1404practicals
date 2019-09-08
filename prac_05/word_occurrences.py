word_occurrences = {}

text = input("Text: ")

words = text.split(" ")

for word in words:
    count = words.count(word)
    word_occurrences[word] = count

print(word_occurrences)
# print("{}: {}".format(word, word_occurrences))
