import wikipedia

search_phrase = input("Search phrase: ")
while search_phrase != "":
    page = wikipedia.page(search_phrase)
    # print(wikipedia.summary(page))

    print("Title: {}".format(page.title))
    print("Summary: {}".format(page.summary))
    print("URL: {}".format(page.url))

    search_phrase = input("Search phrase: ")
