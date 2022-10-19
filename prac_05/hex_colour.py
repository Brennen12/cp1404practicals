def main():
    colour_to_hexadecimal = {"aqua": "#00ffff", "aureolin": "#fdee00", "black": "#000000", "amber": "#ffbf00",
                             "amethyst": "#9966cc", "apricot": "#fbceb1", "beaver": "#9f8170", "beige": "#f5f5dc",
                             "bistre": "#3d2b1f", "celadon": "#ace1af"}
    print(colour_to_hexadecimal)
    for colour, hexadecimal in colour_to_hexadecimal.items():
        print(f"{colour:3} is {hexadecimal}")
    colour_name = input("Enter colour name: ").lower()
    while colour_name != "":
        try:
            print(colour_name, "is", colour_to_hexadecimal[colour_name])
        except KeyError:
            print("Invalid colour name")
        colour_name = input("Enter colour name: ").lower()


main()
