def main():
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)    
    num_words = get_num_words(book_text)
    char_count = get_char_count(book_text)
    sorted_chars = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))

    print(book_text)
    print(char_count)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document.\n")
    for key, value in sorted_chars.items():
        if key.isalpha():
            print(f"The {key} character was found {value} times")

    print("--- End report ---")


def get_num_words(text: str) -> int:
    return len(text.split())

def get_book_text(book_path: str) -> str:
    with open(book_path) as f:
        book_text = f.read()
    return book_text

def get_char_count(text: str) -> dict:
    text_lower = text.lower()
    text_characters = set(text_lower)
    char_count = {}
    for item in text_characters:
        char_count[item] = text_lower.count(item)

    return char_count

if __name__ == '__main__':
    main()