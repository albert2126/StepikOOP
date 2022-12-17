class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}"


class Recipe:
    def __init__(self, *ingrs):
        self.__ingrs = list(ingrs)

    def add_ingredient(self, ing):
        self.__ingrs.append(ing)

    def remove_ingredient(self, ing):
        del self.__ingrs[self.__ingrs.index(ing)]

    def get_ingredients(self):
        return tuple(self.__ingrs)

    def __len__(self):
        return len(self.__ingrs)


# Test 1:
# recipe = Recipe()
# recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
# recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
# recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
# ings = recipe.get_ingredients()
# n = len(recipe) # n = 3
# print(ings, n)

# Test 2:
i1 = Ingredient("Соль", 1, "столовая ложка")
i2 = Ingredient("Мука", 1, "кг")
i3 = Ingredient("Мясо баранины", 10, "кг")
i4 = Ingredient("Масло", 100, "гр")
recipe = Recipe(i1, i2, i3)
recipe.add_ingredient(i4)
recipe.remove_ingredient(i3)

assert len(recipe) == 3, "функция len вернула неверное значение"
lst = recipe.get_ingredients()
for x in lst:
    assert isinstance(x, Ingredient), "в списке рецептов должны быть только объекты класса Ingredient"
    assert hasattr(x, 'name') and hasattr(x, 'volume') and hasattr(x, 'measure'), "объект класса Ingredient должен иметь атрибуты: name, volume, measure"
print(str(i4))
assert str(i4) == "Масло: 100, гр", "метод __str__ вернул неверное значение"

i4 = Ingredient("Масло", 120, "гр")
recipe.add_ingredient(i4)
assert len(recipe) == 4, "функция len вернула неверное значение"
