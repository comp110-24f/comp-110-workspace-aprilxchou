"""Writing for loops"""

pets: list[str] = ["Louie", "Bo", "Bear"]
for animal in pets:
    print(f"Good boy, {animal}!")

names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for index in range(0, len(names)):
    print(str(index) + ":" + names[index])
