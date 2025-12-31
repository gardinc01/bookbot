import sys
from stats import get_num_words, characters, sorting


def get_book_text(path_to_book):
    with open(path_to_book) as f:
        return f.read()


def main():

    if len(sys.argv) != 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_book = sys.argv[1]
    
    text = get_book_text(path_to_book)

    num_words = get_num_words(text)
    chars = characters(text)
    sorted_chars = sorting(chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        ch = item["char"]
        count = item["num"]
        
        if ch.isalpha():
            print(f"{ch}: {count}")
        

    print("============= END ===============")

if __name__ == "__main__":
    main()