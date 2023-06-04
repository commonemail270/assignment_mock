def non_rep(s):
    char_count = {}

    # Count the occurrences of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first non-repeating character and return its index
    for ind, char in enumerate(s):
        if char_count[char] == 1:
            return ind

    return -1
