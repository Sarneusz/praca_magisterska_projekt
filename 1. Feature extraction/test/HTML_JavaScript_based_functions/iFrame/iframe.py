# 15. IFrame Redirection (iFrame)
import re


def iframe(response):
  if response == "":
      return 1
  else:
      if re.findall(r"[|]", response.text):
          return 0
      else:
          return 1

response = """
<!DOCTYPE html>
<html>
<head>
    <title>Page Title</title>   
</head>
<body>
    <h1>This is a Heading</h1>
    <p>This is a paragraph.</p>
    <iframe src="https://www.w3schools.com">
        <p>Your browser does not support iframes.</p>
    </iframe>
"""


iframe(response)