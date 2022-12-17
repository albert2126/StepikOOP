class Video:
    def create(self, name):
        self.name = name

    def play(self):  # для воспроизведения видео (метод выводит на экран строку "воспроизведение видео <name>").
        print(f"воспроизведение видео {self.name}")


class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx):
        cls.videos[video_indx].play()


v1, v2 = Video(), Video()
v1.create('Python')
v2.create('Python ООП')
YouTube.add_video(v1)
YouTube.add_video(v2)
YouTube.play(1)
YouTube.play(2)
