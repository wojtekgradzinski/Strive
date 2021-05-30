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
