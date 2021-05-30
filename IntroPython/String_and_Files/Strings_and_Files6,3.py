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

if __name__ == '__main__':
    import doctest
    print(doctest.testmod(verbose=True))
