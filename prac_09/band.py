from prac_09.musician import Musician


class Band:
    def __init__(self, name=""):
        """Construct a Band with a name and no musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({self.musicians})"

    def __repr__(self):
        return str(self)

    def add(self, musician):
        """Add a musician to the band"""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the instrument playing their first (or no) instrument."""
        band_players = []
        for musician in self.musicians:
            if not musician.instruments:
                band_players.append(f"{musician.name} needs an instrument!\n")
            else:
                band_players.append(f"{musician.name} is playing: {musician.instruments[0]}\n")
        return ''.join(band_players)
