def display(vals: list[int]) -> None:
    idx: int = 0
    while idx < len(vals):
        print(vals[idx])
        idx += 1


display([1, 2, 3])


def odds_lists(min: int, max: int) -> list[int]:
    """Returns list of odds between min and max"""
    odds: list[int] = list()
    x: int = min
    while x <= max:
        if x % 2 == 1:
            odds.append(x)
        x += 1
    return odds


global_odds: list[int] = odds_lists(2, 10)
print(global_odds)


def remove_first(xs: list[str]):
    xs.pop(0)


course: list[str] = ["Comp", "110"]
remove_first(course)
