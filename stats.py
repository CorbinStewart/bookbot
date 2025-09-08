def word_counter(text):
    words = text.split()
    word_count = len(words)
    return word_count


def lowercase_counter(text):
    unique_letters = {}
    words = text.lower()
    for letters in words:
        if letters in unique_letters:
            unique_letters[letters] += 1
        else:
            unique_letters[letters] = 1
    return unique_letters

def sort_letters(unique_letters):
    letter_list = []
    for letters in unique_letters:
        nums = unique_letters[letters]
        letter_list.append({"letters": letters, "num": nums})
    def num_helper(number):
        return number["num"]
    letter_list.sort(key=num_helper, reverse=True)
    return letter_list