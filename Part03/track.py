class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.x = to_x
        self.y = to_y
        self.max_speed = max_speed


class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.tracks = []

    def __len__(self):
        if not len(self.tracks):
            return 0
        t = self.get_tracks()
        first = ((t[0].x - self.start_x) ** 2 + (t[0].y - self.start_y) ** 2) ** 0.5
        return int(sum([((t[i].x - t[i-1].x) ** 2 + (t[i].y - t[i-1].y) ** 2) ** 0.5 for i in range(1, len(t))]) + first)

    def add_track(self, tr):
        self.tracks.append(tr)

    def get_tracks(self):
        return self.tracks

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)


track1 = Track(0, 0)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2 = Track(0, 1)
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2
print(res_eq)
print(len(track1), len(track2))
print(track1 == track2)
