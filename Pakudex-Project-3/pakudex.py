from pakuri import Pakuri


class Pakudex:

    def __init__(self, capacity=20):
        self.capacity = capacity
        self.storage = []

    def get_size(self):
        return len(self.storage)

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):
        if self.storage:
            species_array = []
            for i in range(len(self.storage)):
                species_array.append(self.storage[i].get_species())
            return species_array
        else:
            return None

    def get_stats(self, species):
        if self.storage:
            for i in range(len(self.storage)):
                if self.storage[i].get_species() == species:
                    return [self.storage[i].get_attack(), self.storage[i].get_defense(), self.storage[i].get_speed()]
            return None
        else:
            return None

    def sort_pakuri(self):
        if self.storage:
            species_array = []
            for i in range(len(self.storage)):
                species_array.append(self.storage[i].get_species())
            species_array.sort()
            new_pakudex = []
            for i in range(len(species_array)):
                for j in range(len(self.storage)):
                    if self.storage[j].get_species() == species_array[i]:
                        new_pakudex.append(self.storage[j])
                        break
            self.storage = new_pakudex

    def add_pakuri(self, species):
        if self.storage:
            for i in range(len(self.storage)):
                if self.storage[i].get_species() == species:
                    return False
        try:
            pakuri = Pakuri(species)
            self.storage.append(pakuri)
            return True
        except:
            return False

    def evolve_species(self, species):
        if self.storage:
            for i in range(len(self.storage)):
                if self.storage[i].get_species() == species:
                    try:
                        Pakuri.evolve(self.storage[i])
                        return True
                    except:
                        return False
            return False
        else:
            return False

    def __lt__(self, other):  # ex: Achu.get_name() < Pichu.get_name()
        if self.get_species() < other.get_species():
            i = input()
