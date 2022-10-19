filename = "wimbledon.csv"


def main():
    data = load_data()
    display_winners_count(data)
    display_winning_countries(data)


def load_data():
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        data = [data.strip() for data in in_file.readlines()]
    return data


def display_winners_count(data):
    winners = [record.split(",")[2] for record in data]

    winner_to_count = {}
    for winner in winners:
        winner_to_count[winner] = winner_to_count.get(winner, 0) + 1

    max_length = max(len(winner) for winner in list(winner_to_count.keys()))

    print("Wimbledon Champions:")
    for winner, count in winner_to_count.items():
        print(f"{winner:{max_length}} : {count:>3}")


def display_winning_countries(data):
    countries = sorted(set([record.split(",")[1] for record in data]))
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


main()
