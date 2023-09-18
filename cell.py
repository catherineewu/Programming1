import copy


class Cell:
    def __init__(self, initial_value, row, col):
        self.row = row
        self.col = col
        self.initial_value = initial_value

        self.sketched_value = None
        self.value = copy.deepcopy(initial_value)

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value


"""
    def draw(self):  # FIXME, VISUAL
        # Draws cell and value inside (displayed if != 0).
        # Cell outlined in red if currently selected.
        pass
"""