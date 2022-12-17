class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    def mass(self):
        return self.ro * self.volume

    def __eq__(self, other):
        other = other if isinstance(other, (int, float)) else other.mass()
        return self.mass() == other

    def __lt__(self, other):
        other = other if isinstance(other, (int, float)) else other.mass()
        return self.mass() < other

    def __le__(self, other):
        other = other if isinstance(other, (int, float)) else other.mass()
        return self.mass() <= other

