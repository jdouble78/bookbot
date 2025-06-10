import sys
from stats import word_count, get_book_text, char_count, sorted_dictionary

def main():
        if len(sys.argv) != 2:
              print("Usage: python3 main.py <path_to_book>")
              sys.exit(1)

        book_path = sys.argv[1]

        text = get_book_text(book_path)
        words_count = word_count(text)
        chars_count = char_count(text)
        sorted_count = sorted_dictionary(chars_count)
       
        print("=========== BOOKBOT ===========")
        print(f"Analyzing book found at {book_path}…")
        print("--------- Word Count ----------")
        print(f"Found {words_count} total words")
        print("------- Character Count -------")
        for entry in sorted_count:
            print(f"{entry['char']}: {entry['num']}")
        print("===========   END   ===========")

main()