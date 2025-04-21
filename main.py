from stats import get_num_words, count_letters

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    text = get_book_text('books/frankenstein.txt')
    word_count =  get_num_words(text)
    letter_count = count_letters(text)
    print(f'{word_count} words found in the document')
    print(letter_count)


main()