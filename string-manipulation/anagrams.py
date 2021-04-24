def makeAnagram(a, b):

    """ Create dictionary for each string, for example:
    { "a": 1, "b": 1, "c": 1 }
    { "a": 1, "b": 1, "c": 1, "d": 1 } 
    """

    # Define dictionaries for each string -- use to track num of occurences of each char
    aDict = {}
    bDict = {}

    # Loop through each string
    for char in a:
        if char in aDict:
            aDict[char] += 1
        else:
            aDict[char] = 1

    for char in b:
        if char in bDict:
            bDict[char] += 1
        else:
            bDict[char] = 1

    numOfDel = 0
    # Calculate number of deletions that need to be made
    for i in aDict:
        # Case where char is not present in other string
        if i not in bDict:
            numOfDel += aDict[i]
        # Case where char is present in other string but frequencies differ
        elif aDict[i] != bDict[i]:
            numOfDel += abs(aDict[i] - bDict[i])

    for i in bDict:
        if i not in aDict:
            numOfDel += bDict[i]

    return numOfDel

res = makeAnagram("abbcddeeeeeeeeeeeeeeeeeeeeeeeeee", "abcsbdhdfahjhbcccccvdhbniewfmweeeeeeeeec")
print(res)

""" Different length
abc, abcd or abc, abcc

Different Freq
abb, ab
abb, abbb
abb, art

Same length
abc, abd
abc, abb  """