filename = "wimbledon.csv"


def main():
    lines = load_data()
    display_winners_count(lines)
    display_winning_countries(lines)


def load_data():
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        lines = [line.strip() for line in in_file.readlines()]
    return lines


def display_winners_count(lines):
    winners = [line.split(",")[2] for line in lines]

    winner_to_count = {}
    for winner in winners:
        winner_to_count[winner] = winner_to_count.get(winner, 0) + 1

    max_length = max(len(winner) for winner in list(winner_to_count.keys()))

    print("Wimbledon Champions:")
    for winner, count in winner_to_count.items():
        print(f"{winner:{max_length}} : {count:>3}")


def display_winning_countries(lines):
    countries = sorted(set([line.split(",")[1] for line in lines]))
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


main()
