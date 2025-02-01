def main():
    print("--- Begin report of books/frankenstein.txt ---")

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        char_totals = count_characters(file_contents)
        sorted_characters = sorted(char_totals.items(), key=lambda x: x[1], reverse=True)
        
        print(f"{len(words)} words found in the document")
        for char, count in sorted_characters:
            print(f"The '{char}' character was found '{count}' times")
        print("--- End report ---")

def count_characters(characters):

    char_count = {}
    for character in characters:
        character = character.lower()
        if character.isalpha():
            if character in char_count:
                char_count[character] += 1
            else:
                char_count[character] = 1
    return char_count


    



#if __name__ == "__main__":
main()