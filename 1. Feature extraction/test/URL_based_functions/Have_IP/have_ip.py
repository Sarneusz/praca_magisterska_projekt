import ipaddress
import re


# 2.Checks for IP address in URL (Have_IP)
def havingIP(url):
    try:
        if url.startswith('http://') or url.startswith('https://'):
            url = re.sub(r'https?://', '', url)
        ipaddress.ip_address(url)
        ip = 1
    except:
        ip = 0
    return ip


print(havingIP("https://example.com"))  # Expected to return 0
print(havingIP("192.168.1.1"))  # Expected to return 1
print(havingIP("http://192.168.1.1"))  # Expected to return 1