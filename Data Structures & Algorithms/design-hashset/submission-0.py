class MyHashSet:

    def __init__(self):
        # direct addressing table
        self.table = [False] * (10**6 + 1)

    def add(self, key: int) -> None:
        self.table[key] = True

    def remove(self, key: int) -> None:
        self.table[key] = False

    def contains(self, key: int) -> bool:
        return self.table[key]
