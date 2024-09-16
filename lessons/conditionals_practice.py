"""More practice with conditionals."""


def get_weather_report() -> str:
    """Give advice based on the weather"""
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    if weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather")
    return weather
