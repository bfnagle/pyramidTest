def build_letter_count_map(word):
    letter_count = {}
    for letter in word:
        if letter not in letter_count:
            letter_count[letter] = 0
        letter_count[letter] += 1
    return letter_count

def check_if_pyramid(sorted_letters):
    for i in range(len(sorted_letters)):
        if sorted_letters[i][1] != (i + 1):
            return False
    return True

def is_pyramid(word):
    if len(word) == 0:
        return False
    letter_count = build_letter_count_map(word)
    sorted_letters = sorted(letter_count.items(), key=lambda item: item[1])
    return check_if_pyramid(sorted_letters)

if __name__ == "__main__":
    assert(is_pyramid('banana'))
    assert(not is_pyramid('bandana'))
    assert(not is_pyramid(""))
    assert(is_pyramid("a"))
    assert(is_pyramid("abb"))
    assert(is_pyramid("bab"))
    assert(not is_pyramid("bac"))