# 14.End time of domain: The difference between termination time and current time (Domain_End)
from datetime import datetime


def domainEnd(domain_name):
    expiration_date = domain_name.expiration_date
    if isinstance(expiration_date, str):
        try:
            expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
        except:
            return 1
    if expiration_date is None:
        return 1
    elif type(expiration_date) is list:
        return 1
    else:
        today = datetime.now()
        end = abs((expiration_date - today).days)
        if (end / 30) < 6:
            end = 0
        else:
            end = 1
    return end


# Example
print(domainEnd('google.com'))