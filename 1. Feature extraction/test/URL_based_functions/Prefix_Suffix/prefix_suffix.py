# 9.Checking for Prefix or Suffix Separated by (-) in the Domain (Prefix/Suffix)
from urllib.parse import urlparse


def prefixSuffix(url):
    if '-' in urlparse(url).netloc:
        return 1            # phishing
    else:
        return 0            # legitimate



print(prefixSuffix("https://example.com"))  # Expected to return 0
print(prefixSuffix("https://www-example.com"))  # Expected to return 1
print(prefixSuffix("https://www.example-gov.com"))  # Expected to return 0