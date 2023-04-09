import re

def urlComp(url1, url2):
    # convert strings to lowercase to make comparison case-insensitive
    url1 = url1.lower()
    url2 = url2.lower()

    # split
    regex = re.compile('[a-zA-Z]+')
    wordsUrl1 = regex.findall(url1)
    wordsUrl2 = regex.findall(url2)

    matches = []
    for word in wordsUrl1:
        if word in wordsUrl2:
            matches.append(word)

    return matches

# test function
'''
str1 = "www.hilton.com"
str2 = "www.hilton-hotels.com"
common_part = urlComp(str1, str2)
for element in common_part:
    print(element)
'''