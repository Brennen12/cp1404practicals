"""
Word Occurrences
Estimated: 30 minutes
Actual:
"""


def main():
    words = input("Text: ").split()
    word_to_count = {}
    for word in words:
        word_to_count[word] = word_to_count.get(word, 0) + 1
    max_length = max(len(word) for word in list(word_to_count.keys()))
    for word, count in sorted(word_to_count.items()):
        print(f"{word:{max_length}} : {count:>2}")


main()
