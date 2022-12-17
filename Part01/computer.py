class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, *mem_slots):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = mem_slots

    def get_config(self):
        slots = '; '.join((f'{mem.name} - {mem.volume}' for mem in self.mem_slots))
        return [f'Материнская плата: {self.name}',
                f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                f"Память: {slots}"]


mb = MotherBoard('FakeBoard', CPU('i8', 4800), Memory('Samsung32GB', 32), Memory('Samsung32GB', 32))

# Tests:

# print(mb.get_config())

assert isinstance(mb, MotherBoard) and hasattr(MotherBoard, 'get_config')

def get_config():
    mem_str = "; ".join([f"{x.name} - {x.volume}" for x in mb.mem_slots])

    return [f"Материнская плата: {mb.name}", f"Центральный процессор: {mb.cpu.name}, {mb.cpu.fr}",
            f"Слотов памяти: {mb.total_mem_slots}", f"Память: {mem_str}"]


res1 = ("".join(mb.get_config())).replace(" ", "")
res2 = ("".join(get_config())).replace(" ", "")
assert res1 == res2, "метод get_config возвратил неверные данные"
