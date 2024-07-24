# 13.Survival time of domain: The difference between termination time and creation time (Domain_Age)
from datetime import datetime


def domainAge(domain_name):
    creation_date = domain_name.creation_date
    expiration_date = domain_name.expiration_date
    if isinstance(creation_date, str) or isinstance(expiration_date, str):
        try:
            creation_date = datetime.strptime(creation_date, '%Y-%m-%d')
            expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
        except:
            return 1
    if (expiration_date is None) or (creation_date is None):
        return 1
    elif (type(expiration_date) is list) or (type(creation_date) is list):
        return 1
    else:
        ageofdomain = abs((expiration_date - creation_date).days)
        if (ageofdomain / 30) < 6:
            age = 1
        else:
            age = 0
    return age


# Example
print(domainAge('google.com'))