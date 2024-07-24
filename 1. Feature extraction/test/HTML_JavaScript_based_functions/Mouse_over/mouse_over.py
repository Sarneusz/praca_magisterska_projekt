# 15. IFrame Redirection (iFrame)
# 16.Checks the effect of mouse over on status bar (Mouse_Over)
import re


def mouseOver(response):
    if response == "":
        return 1
    else:
        if re.findall("", response.text):
            return 1
        else:
            return 0
