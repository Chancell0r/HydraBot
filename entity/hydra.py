from .attacker import Attacker

HYDRA_HEALTH = {
    "hydra1": 5946906,
    "hydra2": 17699730,
    "hydra3": 54533157,
    "hydra4": 106981939,
    "hydra5": 220606896
}

HYDRA_ELEMENTS = ['light', 'darkness', 'earth', 'water', 'fire', 'wind']


class Hydra(object):

    def __init__(self, hydra_type: str, element: str):
        self.hydra_type = hydra_type
        self.element = element
        self.health_remaining = HYDRA_HEALTH[hydra_type]
        self.attackers = []

    def add_attacker(self, attacker: Attacker):
        try:
            self.attackers.index(attacker)
        except ValueError:
            self.attackers.append(attacker)
            self.attackers.sort()

    def remove_attacker(self, order):
        for i in range(len(self.attackers)):
            if self.attackers[i].order == order:
                del self.attackers[i]

    def use_attack(self, attacker: Attacker):
        try:
            index = self.attackers.index(attacker)
            self.attackers[index].used = True
        except ValueError:
            return

    def set_health_remaining(self, health):
        self.health_remaining = health

    def _attackers_as_string(self):
        string = 'attackers: [\n'
        for attacker in self.attackers:
            string += str(attacker) + '\n'
        string += ']\n'
        return string

    def __str__(self):
        return 'element: %s\n' \
               'health_remaining: %s\n' \
               '%s' % (
                   self.element, str(self.health_remaining), self._attackers_as_string())


def generate_base_hydras():
    base_hydras = dict()
    for key in HYDRA_HEALTH.keys():
        base_hydras[key] = generate_base_hydra(key)

    return base_hydras


def generate_base_hydra(key):
    hydras = []
    for element in HYDRA_ELEMENTS:
        hydra = Hydra(key, element)
        hydras.append(hydra)

    return hydras
