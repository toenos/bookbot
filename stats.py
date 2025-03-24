def get_num_words(text):
    word_count = len(text.split())
    return word_count

def count_chars(text):
    char_count = {}
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char in char_count:
            char_count[lowercase_char] += 1
        else:
            char_count[lowercase_char] = 1
    return char_count

def sort_characters(char_count):
    sorted_chars = []

    for char, count in char_count.items():
        sorted_chars.append({"char": char, "count": count})

    def sort_on(dict):
        return dict["count"]

    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars
