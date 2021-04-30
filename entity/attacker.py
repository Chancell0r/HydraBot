class Attacker(object):

    def __init__(self, name: str, order: int, used: bool):
        self.name = name
        self.order = order
        self.used = used

    def __lt__(self, other):
        return self.order < other.order

    def __eq__(self, other):
        return self.order == other.order

    def __str__(self):
        return 'name: %s, order: %s, used: %s' % (self.name, str(self.order), str(self.used))
