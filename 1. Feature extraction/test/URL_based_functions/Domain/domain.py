from urllib.parse import urlparse
import re


# 1.Domain of the URL (Domain)
def getDomain(url):
    domain = urlparse(url).netloc
    if re.match(r"^www.", domain):
        domain = domain.replace("www.", "")
    return domain


print(getDomain("https://eevee.tv/Bootstrap/assets/css/acces"))
print(getDomain("https://firebasestorage.googleapis.com"))