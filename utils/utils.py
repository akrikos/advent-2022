import re


def parse_ints(line: str) -> list:
    return list(map(int, re.findall('\d+', line)))
