from stats import get_num_words
from stats import get_char_frequency
from stats import get_sorted_dictionary
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]    
    book_content = get_book_text(book_path)
    num_words = get_num_words(book_content)
    char_freq = get_char_frequency(book_content)
    sorted_freq = get_sorted_dictionary(char_freq)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_freq:
        if item['char'].isalpha() is True:
            print(f"{item['char']}: {item['num']}")

main()