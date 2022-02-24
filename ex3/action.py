class BaseAction:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class NothingAction(BaseAction):
    def __init__(self):
        super().__init__('Nothing')

    def __gt__(self, other):
        return 0


class RockAction(BaseAction):
    def __init__(self):
        super().__init__('Rock')

    def __gt__(self, other):
        return 1 if isinstance(other, ScissorsAction) else 0


class PaperAction(BaseAction):
    def __init__(self):
        super().__init__('Paper')

    def __gt__(self, other):
        return 1 if isinstance(other, RockAction) else 0


class ScissorsAction(BaseAction):
    def __init__(self):
        super().__init__('Scissors')

    def __gt__(self, other):
        return 1 if isinstance(other, PaperAction) else 0
