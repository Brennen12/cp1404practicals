import wikipedia

search_phrase = input("Enter a page title or phrase: ")

while search_phrase:
    try:
        results = wikipedia.page(search_phrase, auto_suggest=False)
        print(results.title)
        print(results.summary)
        print(results.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    search_phrase = input("Enter a page title or phrase: ")
