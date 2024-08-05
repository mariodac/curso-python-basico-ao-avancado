import re

NUM_OR_DOT_REGEX = re.compile(r'[0-9.]')

def isValidNumber(string: str):
    try:
        float(string)
        return True
    except:
        return False

def isNumOrDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))

def isEmpty(string: str):
    return string.strip() == ''

