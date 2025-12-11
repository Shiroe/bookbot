import sys
from stats import (
    get_number_of_words,
    get_all_characters_occurence,
    get_characters_occurence_sorted,
)


def get_book_text(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_path = ""

    args = sys.argv

    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = args[1]
        book_text = get_book_text(book_path)
        num_words = get_number_of_words(book_text)
        ch_occur = get_all_characters_occurence(book_text)
        occur_sorted = get_characters_occurence_sorted(ch_occur)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")

        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")

        print("--------- Character Count -------")
        for item in occur_sorted:
            print(f"{item['char']}: {item['num']}")

        print("============= END ===============")


main()
