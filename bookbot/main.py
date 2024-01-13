def main():
    path = "books/frankenstein.txt"
    contents = get_book_contents(path)

    print(f"--- Begin report of {path} ---")
    words_count = get_words_count(contents)
    print(f"{words_count} words found in the document\n")
    chars_count = get_chars_count(contents)

    chars_list = list(chars_count.items())
    chars_list.sort(key=lambda x: x[1], reverse=True)

    for char in chars_list:
        if char[0].isalpha():
            print(f"The '{char[0]}' character was found {char[1]} times")

    print("--- End report ---")

def get_book_contents(path):
    with open(path) as f:
        return f.read()

def get_words_count(text):
    return len(text.split())

def get_chars_count(text):
    chars = {}

    for char in text:
        c = char.lower()
        if not c in chars:
            chars[c] = 0

        chars[c] += 1

    return chars

main()
