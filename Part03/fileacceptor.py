class FileAcceptor:
    def __init__(self, *extensions):
        self.exts = extensions

    def __call__(self, fname: str):
        return fname.split('.')[-1] in self.exts

    def __add__(self, other):
        return FileAcceptor(*tuple(set(self.exts + other.exts)))


# Tests:
acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2    # ("jpg", "jpeg", "png", "bmp")
print(acceptor12.exts)
acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = ["boat.jpg", "test.tst", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]
filtered_names = list(filter(acceptor_images + acceptor_docs, filenames))
print(filtered_names)
