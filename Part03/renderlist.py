class RenderList:
    def __init__(self, type_list: str):
        self.type_list = 'ol' if type_list == 'ol' else 'ul'

    def __call__(self, items: list):
        html_items = '\n'.join([f"<li>{item}</li>" for item in items])
        return f"<{self.type_list}>\n{html_items}\n</{self.type_list}>"


# Test:
lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)