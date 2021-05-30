def index_vowels(text):
    """
    String -> Dictionary
    Take a string and associate each letter to its pos

    >>> index_vowels('')
    {}
    >>> index_vowels('Hello')
    {'e': 1, 'o': 4}
    """
    d = {}
    f_text = text.casefold()
    for i, c in enumerate(f_text):
        if f_text[i] == 'a' or f_text[i] == 'e' or f_text[i] == 'i' or f_text[i] == 'o' or f_text[i] == 'u':
            d[c] = i
    return d

def similar_char(s1, s2):
    """
    String, String -> ListOfString
    >>> similar_char("The holy Grail", "Life of Brian")
    ['o in position 5', 'a in position 11']
    """
    los = []
    str1, str2 = s1.casefold(), s2.casefold()
    if len(str1) <= len(str2):
        shorter_str, longer_str = str1, str2
    else:
        shortest_str, longer_str = str2, str1
    for i, c in enumerate(shortest_str):
        if shortest_str[i] == longer_str[i]:
            los.append(str(c) + " in position " + str(i))
    return los

def helper_to_distill(text):
    """
    String -> String
    Returs only text found within pairs of square bracket
    >>> distill("example[ string]")
    (' string', 16)
    """
    open_bracket = text.find('[')
    close_bracket = text.find(']', open_bracket + 1)
    if close_bracket == -1:
        return None
    else:
        string = text[open_bracket + 1: close_bracket]
        next_string_pos = close_bracket + 1
    return string, next_string_pos

# def distill_all(text):
#     """
#     String -> String
#     >>> distill("[a]n example [ string] ")
#     "a string"
#     """
#     los = []
#     while True:
#         string, next_string_pos = helper_to_distill(text)
#         if string:
#             los.append(string)
#             # next_string, next_string_pos = distill(text[next_string_pos:])
#             #
#             text = text[next_string_pos:]
#         else:
#             break
#     concatenated_strings = " ".join(los)
#     return concatenated_strings

if __name__ == '__main__':
    import doctest
    print(doctest.testmod(verbose=True))
