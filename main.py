import sys
from stats import get_num_words
from stats import count_chars
from stats import sort_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
        
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    charcount = count_chars(book_text)

    sorted_char_list = sort_characters(charcount)

    for item in sorted_char_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")

main()

