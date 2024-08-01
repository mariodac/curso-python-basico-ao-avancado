import re

NUM_OR_DOT_REGEX = re.compile(r'[0-9.]')

def isNumOrDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))

def isEmpty(string: str):
    return string.strip() == ''

