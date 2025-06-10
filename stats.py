def word_count(book_text):
    count = len(str.split(book_text))
    return count

def get_book_text(book_file_path):
    with open(book_file_path) as f:
        contents = f.read()
    return contents

def char_count(book_text):
    converted = book_text.lower()
    count_dictionary = {}
    for i in converted:
        if i not in count_dictionary:
            count_dictionary[i] = 1
        else:
            count_dictionary[i] += 1
    return count_dictionary

def sorted_dictionary(count_dict):
    items = [
        {"char": char, "num": count}
        for char, count in count_dict.items()
        if char.isalpha()
    ]

    items.sort(key=lambda x: x["num"], reverse=True)

    return items