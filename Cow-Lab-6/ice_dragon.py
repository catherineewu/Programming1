from dragon import Dragon


class IceDragon(Dragon):
    def __init__(self, name, image):
        Dragon.__init__(self, name, image)

    @staticmethod
    def can_breathe_fire():
        return False
