# 6.Checking for redirection '//' in the url (Redirection)
def redirection(url):
    pos = url.rfind('//')
    if pos > 6:
        if pos > 7:
            return 1
        else:
            return 0
    else:
        return 0


print(redirection("https://example.com"))  # Expected to return 0
print(redirection("https://example.com//"))  # Expected to return 1
print(redirection("https://example.com/"))  # Expected to return 0