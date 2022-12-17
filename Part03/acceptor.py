class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, fname):
        return fname.split('.')[-1] in self.extensions


# Test 1:
# filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
# acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
# image_filenames = filter(acceptor, filenames)
# print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]

# Test 2:
fs = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.8.jpg", "forest.jpeg", "eq_1.png", "eq_2.png", "my.html", "data.shtml"]
acceptor = ImageFileAcceptor(("jpg", "png"))
res = filter(acceptor, fs)
print(set(res))
print(set(["boat.jpg", "web.png", "ava.8.jpg", "eq_1.png", "eq_2.png"]))
assert set(res) == set(["boat.jpg", "web.png", "ava.8.jpg", "eq_1.png", "eq_2.png"]), "с помощью объекта класса ImageFileAcceptor был сформирован неверный список файлов"

acceptor = ImageFileAcceptor(("jpeg", "html"))
res = filter(acceptor, fs)
assert set(res) == set(["forest.jpeg", "my.html"]), "с помощью объекта класса ImageFileAcceptor был сформирован неверный список файлов"
