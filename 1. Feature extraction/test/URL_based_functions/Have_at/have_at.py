# 3.Checks the presence of @ in URL (Have_At)
def haveAtSign(url):
    if "@" in url:
        at = 1
    else:
        at = 0
    return at


print(haveAtSign("https://example.com"))  # Expected to return 0
print(haveAtSign("https://example@.com"))  # Expected to return 1
print(haveAtSign("example.com@wp.pl"))  # Expected to return 1