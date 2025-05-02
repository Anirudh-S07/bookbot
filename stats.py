# This file has the function to count the number of lines from a string input called words

def get_num_of_words(words:str):
    list_of_words = []
    list_of_words = words.split()
    return len(list_of_words)


def repeating_characters(words:str):
    set_to_lower = words.lower()
    dict = {}
    for char in set_to_lower:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] =1

    return(dict) 

def sorted_list_of_dict(dict:dict):
    list = []
    for item in dict:
        new_dict={}
        new_dict["char"] = item
        new_dict["num"] = dict[item]
        list.append(new_dict)
    list.sort(reverse=True, key=lambda dict: dict["num"])
    return list






