def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def word_count(book_text):
    num_words = len(book_text.split())
    return num_words

def character_count(book_text):
    character_dictionary = {}
    for c in book_text.lower():
        if c in character_dictionary:
            character_dictionary[c] = character_dictionary[c] + 1
        else:
            character_dictionary[c] = 1
    return character_dictionary

def sort_on(d):
    return d["num"]

def character_sort(character_dictionary):
    characters = []
    for d in character_dictionary:
        characters.append({"char": d, "num": character_dictionary[d]})
    characters.sort(reverse=True, key=sort_on)
    return characters