import re

# эти строчки не менять
stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]


class StringText:
    def __init__(self, lst_words):
        self.lst_words = lst_words

    def __lt__(self, other):
        return len(self.lst_words) < len(other.lst_words)

    def __le__(self, other):
        return len(self.lst_words) <= len(other.lst_words)


w_lst = [re.sub(r'[–?!,.;]', r'', line).split() for line in stich]
lst_text = [StringText(line) for line in w_lst]
print(*lst_text)
lst_text_sorted = sorted(lst_text, reverse=True)
print()
print(*lst_text_sorted)
lst_text_sorted = [' '.join(obj.lst_words) for obj in lst_text_sorted]
print(*lst_text_sorted, sep='\n')
