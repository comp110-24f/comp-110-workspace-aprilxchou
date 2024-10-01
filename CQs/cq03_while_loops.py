"""While Loops Challenge Question"""

__author__ = "730754347"


def num_instances(phrase: str, search_char: str) -> int:
    """Searches for character occurrence in phrase"""
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if search_char == phrase[index]:
            count = count + 1
            index = index + 1
        else:
            index = index + 1
    return count


print(num_instances(phrase="HelloHello", search_char="e"))
