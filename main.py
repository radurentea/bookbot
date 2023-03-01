from collections import Counter

book = input("Enter file path of the book: ")

with open(f"{book}") as f:
    file_contents = f.read()

def count_words(text):
    words = text.split()
    words_count = len(words)

def count_letters(text):
    alpha_text = ""
    for i in text:
        if i.isalpha():
            alpha_text += i

    lower_text = alpha_text.lower()
    counters = Counter(lower_text)
    counters_arr = list(counters.items())
    arr = [(char, num) for num, char in counters_arr]
    return sorted(arr, reverse=True)

def create_report(words, letters):
    print(f"--- Begin report of {book} ---")
    print(f"{words} words found in the document")
    print("\n")
    for letter in letters:
        print(f"The '{letter[1]}' character was found {letter[0]} times")
    print("---  End report ---")


words = count_words(file_contents)
letters = count_letters(file_contents)
create_report(words, letters)