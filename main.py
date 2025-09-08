import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import word_counter, lowercase_counter, sort_letters

def main():
    path_to_book = sys.argv[1]
    text = get_book_text(path_to_book)
    num_words = word_counter(text)
    letter_count = lowercase_counter(text)
    letter_list = sort_letters(letter_count)
    final_list = []
    for entry in letter_list:
        letter = entry["letters"]
        count = entry["num"]
        if letter.isalpha():
            final_list.append(f"{letter}: {count}")        
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in final_list:
        print(entry)
    print("============= END ===============")

    
def get_book_text(path_to_book):
    with open(path_to_book) as f:
        return f.read()

main()