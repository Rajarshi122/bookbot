from stats import get_num_words, count_letters, sorted_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    text = get_book_text(sys.argv[1])
    word_count =  get_num_words(text)
    letter_count = count_letters(text)
    chars = sorted_list(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print(f'----------- Word Count ---------- \nFound {word_count} total words')
    #print(letter_count)
    print('--------- Character Count -------')
    for char, char_count in chars.items():
        if char.isalpha():
            print(f'{char}: {char_count}')


main()