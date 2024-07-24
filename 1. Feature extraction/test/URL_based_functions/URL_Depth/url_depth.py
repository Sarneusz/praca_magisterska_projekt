# 5.Gives number of '/' in URL (URL_Depth)
from urllib.parse import urlparse


def getDepth(url):
    s = urlparse(url).path.split('/')
    depth = 0
    for j in range(len(s)):
        if len(s[j]) != 0:
            depth = depth+1
    return depth


print(getDepth("https://example.com"))  # Expected to return 0
print(getDepth("https://example.com/Bootstrap/assets/css/acces"))  # Expected to return 4