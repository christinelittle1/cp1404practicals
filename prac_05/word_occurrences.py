word_occurrences = {}

text = input("Text: ")
words = text.split(" ")
words.sort()

for word in words:
    count = words.count(word)
    word_occurrences[word] = count

length_of_longest_word = max((len(word) for word in words))

for word in word_occurrences:
    print("{:{}} : {}".format(word, length_of_longest_word, word_occurrences[word]))
