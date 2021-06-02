def twoStrings(s1, s2):
    present_chars = {}
    for c in s1:
        present_chars[c] = 1
    for c in s2:
        try:
            present_chars[c]
            return "YES"
        except KeyError:
            continue

    return "NO"
