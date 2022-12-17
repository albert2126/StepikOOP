class Morph:
    def __init__(self, *words):
        self.__words = words

    def __eq__(self, word):
        return word.lower() in self.__words

    def add_word(self, word):
        self.__words += (word,)

    def get_words(self):
        return self.__words

dict_words = [Morph('связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях'),
              Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами', 'формулах'),
              Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам', 'векторами', 'векторах'),
              Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам', 'эффектами', 'эффектах'),
              Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')]

text = input()
print(sum([1 for word in text.split() if word.strip(' ,.') in dict_words]))


# print(sum([1 for word in text.split() if any([morph == word.strip(' ,.') for morph in dict_words])]))
print('связь' == dict_words[0])
