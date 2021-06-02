def checkMagazine(magazine, note):
    present_words = {}
    for i in magazine:
        if i not in present_words:
            present_words[i] = 1
        else:
            present_words[i] += 1

    try:
        for i in note:
            present_words[i] -= 1
            if present_words[i] < 0:
                return "No"
    except KeyError:
        return "No"

    return "Yes"
