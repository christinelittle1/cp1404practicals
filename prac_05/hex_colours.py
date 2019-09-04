HEX_COLOUR_CODES = {"black": "#000000", "brown": "#a52a2a", "coral": "#ff7f50", "magenta": "#ff00ff",
                    "orchid": "#da70d6", "pink": "#ffc0cb", "SkyBlue": "#87ceeb", "white": "ffffff",
                    "YellowGreen": "9acd32", "SlateBlue": "#6a5acd"}

colour_name = input("Enter colour name: ")
while colour_name != "":
    if colour_name in HEX_COLOUR_CODES:
        print(HEX_COLOUR_CODES[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ")
