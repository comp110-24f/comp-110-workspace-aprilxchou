"""Implement utility functions."""

__author__ = "730754347"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Invert dictionary keys and values"""
    output: dict[str, str] = {}
    for key in input:
        value: str = input[key]
        if value in output:  # means duplicate exists
            raise KeyError(
                "This value exists multiple times, so it cannot become a key"
            )
        output[value] = key
    return output


def favorite_color(a: dict[str, str]) -> str:
    """Return most said color in a dict."""
    fav: str = ""
    color_count: dict[str, int] = {}  # color and count
    max: int = 0  # keep track of max count
    for name in a:  # will count favorite colors and put in a dict
        if a[name] in color_count:
            color_count[a[name]] += 1
        else:
            color_count[a[name]] = 1
    for color in color_count:
        if color_count[color] > max:  # compares colors singularly
            fav = color  # will only reassign if greater than, not equal to max
            max = color_count[color]
    return fav


def count(initial: list[str]) -> dict[str, int]:
    """Counts number of each word in list"""
    final: dict[str, int] = {}
    for elem in initial:
        if elem in final:
            final[elem] += 1
        else:
            final[elem] = 1
    return final


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Sorts words by the letters in them"""
    result: dict[str, list[str]] = {}
    for elem in words:
        idx: int = 0
        values: list[str] = []
        if elem[idx].lower() in result:
            result[elem[idx].lower()].append(elem)
        else:
            values.append(elem)
            result[elem[idx].lower()] = values
    return result


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Attendance of students stored in a dict."""
    if day in attendance:
        if not (
            student in attendance[day]
        ):  # if student is not already counted in attendance
            attendance[day].append(student)
    else:
        attendance[day] = [student]  # if day is not already in attendance
