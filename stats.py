# from collections import Counter

def get_num_words(text):
    words_list = text.split()
    return len(words_list)

def get_char_frequency(text):
    chars_frequency = {}
    text_lower = text.lower()
    
    for char in text_lower:
        if char not in chars_frequency:
            chars_frequency[char] = 1
        else:
            chars_frequency[char] += 1

    return chars_frequency

def sort_on(items):
    return items["num"]

def get_sorted_dictionary(dictionary):
    items = []
    for key in dictionary:
        items.append({"char": key, "num": dictionary[key]})

    items.sort(reverse=True, key=sort_on)
    return items
    

# def get_char_frequency(text):
#     text_lower = text.lower()
#     return Counter(text_lower)
