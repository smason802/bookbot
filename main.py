from stats import *
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
        characters = character_sort(character_count(text))
        print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------")
        print(f"Found {word_count(text)} total words")
        print("--------- Character Count -------")
        for d in characters:
            if d["char"].isalpha():
                print(f"{d["char"]}: {d["num"]}")
        print("============= END ===============")

main()