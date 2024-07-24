# 4.Finding the length of URL and categorizing (URL_Length)
def getLength(url):
    if len(url) < 54:
        length = 0
    else:
        length = 1
    return length


print(getLength("https://example.com"))  # Expected to return 0
print(getLength("https://example.com/Bootstrap/assets/css/acces/Bootstrap/assets/css/acces"))  # Expected to return 1