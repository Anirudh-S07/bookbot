# This file contains the function for open and reading a file the function itself will be called by the main command
from stats import get_num_of_words, repeating_characters, sorted_list_of_dict
import sys



def main():
    # Check if sys.argv has two entries
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Use the second argument as the filepath
    filepath = sys.argv[1]
    
    words = get_book_text(filepath)
    num_of_words = get_num_of_words(words)
    dict_of_repeating_letters = repeating_characters(words)
    
    # Print header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    
    # Sort and filter the characters
    sorted_list = sorted_list_of_dict(dict_of_repeating_letters)
    filtered_list = []
    for i in sorted_list:
        if i["char"].isalpha():
            filtered_list.append(i)    

    # Print each character count in the required format
    for item in filtered_list:
        print(f"{item['char']}: {item['num']}")
    
    # Print footer
    print("============= END ===============")





def get_book_text(filepath:str):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

    
main()


