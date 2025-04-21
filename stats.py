def get_num_words(file_contents):
    num_words = len(file_contents.split())
    return num_words


def count_letters(file_contents):
    count_letters ={}
    for num in file_contents:
        nums = num.lower()
        count_letters[nums] = 1 + count_letters.get(nums, 0)
    return count_letters