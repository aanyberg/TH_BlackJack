def color_print(self, color, text, end="\n"):
    color_dict = {
        "black": 30,
        "red": 31,
        "green": 32,
        "yellow": 33,
        "blue": 34,
        "magenta": 35,
        "cyan": 36,
        "white": 37
    }

    color_string = f"\033[{color_dict[color]}m"
    reset_string = f"\033[0m"
    print(f"{color_string}{text}{reset_string}", end=end)
