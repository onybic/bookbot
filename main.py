def main():
    book_path = "./books/fankenstein.txt"
    text = get_text(book_path)
    print(text)
    word_count = get_word_count(text)
    print(f"Word count: {word_count}")
    character_count = get_character_count(text)
    print(f"Character count: {character_count}")

    char_sorted_list = sort_characters(character_count)
    print(f"------------Being report of {book_path}------------")
    print(f"{word_count} words found in the document")
    print()
    for character in char_sorted_list:
        if not character["char"].isalpha():
            continue
        print(f"The '{character['char']}' character was found '{character['num']}' times")

    print("-------- End of report ----------")
def get_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    characters = {}
    lower_string = text.lower()
    for character in lower_string:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

def sort_characters(characters_dict):
    sorted_list = []
    for character in characters_dict:
        sorted_list.append({"char": character, "num": characters_dict[character]})
    sorted_list.sort(reverse=True, key=lambda x: x["num"])
    return sorted_list


main()