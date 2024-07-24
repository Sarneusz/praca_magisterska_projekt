# 7.Existence of “HTTPS” Token in the Domain Part of the URL (https_Domain)
from urllib.parse import urlparse


def httpDomain(url):
    domain = urlparse(url).netloc
    if 'https' in domain:
        return 1
    else:
        return 0


print(httpDomain("https://https-example.com"))  # Expected to return 1
print(httpDomain("http://http-example.com"))  # Expected to return 0
print(httpDomain("https-example.com"))  # Expected to return 0