import sys


class Vertex:
    def __init__(self):
        self._links = []

    @property
    def links(self):
        return self._links

    @links.setter
    def links(self, value):
        self._links = value

    def get_neighbor(self, link):
        for v in (link.v1, link.v2):
            if v != self:
                return v


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Link:
    def __init__(self, v1, v2, dist=1):
        self._v1, self._v2, self._dist  = v1, v2, dist

    @property
    def v1(self):
        return self._v1

    @v1.setter
    def v1(self, value):
        self._v1 = value

    @property
    def v2(self):
        return self._v2

    @v2.setter
    def v2(self, value):
        self._v2 = value

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, value):
        self._dist = value

    def __hash__(self):
        return hash(id(self._v1) + id(self._v2))

    def __eq__(self, other):
        return hash(self) == hash(other)


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2, dist)

    def __str__(self):
        return self.dist

    def __repr__(self):
        return self.dist


class LinkedGraph:
    def __init__(self):
        self._vertex = []
        self._links = []

    def add_vertex(self, v):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        if link not in self._links:
            self._links.append(link)
            if link.v1 not in self._vertex:
                self._vertex.append(link.v1)
            link.v1.links.append(link)
            if link.v2 not in self._vertex:
                self._vertex.append(link.v2)
            link.v2.links.append(link)

    def find_path(self, start_v, stop_v):
        unvisited, shortest, previous = self._vertex.copy(), {}, {}
        max_dist = sys.maxsize
        for v in unvisited:
            shortest[v] = max_dist
        shortest[start_v] = 0
        while unvisited:
            current_min_v = None
            for v in unvisited:
                if not current_min_v:
                    current_min_v = v
                elif shortest[v] < shortest[current_min_v]:
                    current_min_v = v
            for link in current_min_v.links:
                neighbor = current_min_v.get_neighbor(link)
                temp_value = shortest[current_min_v] + link.dist
                if temp_value < shortest[neighbor]:
                    shortest[neighbor] = temp_value
                    previous[neighbor] = current_min_v
            unvisited.remove(current_min_v)
        path, node = [], stop_v
        while node != start_v:
            path.insert(0, node)
            node = previous[node]
        path.insert(0, start_v)
        links = []
        for i in range(len(path) - 1):
            for link in self._links:
                if {link.v1, link.v2} == {path[i], path[i + 1]}:
                    links.append(link)
        return path, links


# Test 1:
map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))
# print(f"V!.links: {v1.links}")
map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))

print(len(map_metro._links))
print(len(map_metro._vertex))
path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
print(path[0])    # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
print(sum([x.dist for x in path[1]]))  # 7


# Test 2:
map2 = LinkedGraph()
v1 = Vertex()
v2 = Vertex()
v3 = Vertex()
v4 = Vertex()
v5 = Vertex()

map2.add_link(Link(v1, v2))
map2.add_link(Link(v2, v3))
map2.add_link(Link(v2, v4))
map2.add_link(Link(v3, v4))
map2.add_link(Link(v4, v5))

assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
assert len(map2._vertex) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"

map2.add_link(Link(v2, v1))
assert len(map2._links) == 5, "метод add_link() добавил связь Link(v2, v1), хотя уже имеется связь Link(v1, v2)"

path = map2.find_path(v1, v5)
s = sum([x.dist for x in path[1]])
assert s == 3, "неверная суммарная длина маршрута, возможно, некорректно работает объект-свойство dist"

assert issubclass(Station, Vertex) and issubclass(LinkMetro, Link), "класс Station должен наследоваться от класса Vertex, а класс LinkMetro от класса Link"

map2 = LinkedGraph()
v1 = Station("1")
v2 = Station("2")
v3 = Station("3")
v4 = Station("4")
v5 = Station("5")

map2.add_link(LinkMetro(v1, v2, 1))
map2.add_link(LinkMetro(v2, v3, 2))
map2.add_link(LinkMetro(v2, v4, 7))
map2.add_link(LinkMetro(v3, v4, 3))
map2.add_link(LinkMetro(v4, v5, 1))

assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
assert len(map2._vertex) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"

path = map2.find_path(v1, v5)

assert str(path[0]) == '[1, 2, 3, 4, 5]', path[0]
s = sum([x.dist for x in path[1]])
assert s == 7, "неверная суммарная длина маршрута для карты метро"
