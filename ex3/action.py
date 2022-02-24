class BaseAction:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __gt__(self, other):
        if isinstance(self, RockAction) and isinstance(other, ScissorsAction):
            return 1
        if isinstance(self, PaperAction) and isinstance(other, RockAction):
            return 1
        if isinstance(self, ScissorsAction) and isinstance(other, PaperAction):
            return 1
        return 0

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.name == other.name

    def __hash__(self):
        return hash(self.name)


class NothingAction(BaseAction):
    def __init__(self):
        super().__init__('Nothing')


class RockAction(BaseAction):
    def __init__(self):
        super().__init__('Rock')


class PaperAction(BaseAction):
    def __init__(self):
        super().__init__('Paper')


class ScissorsAction(BaseAction):
    def __init__(self):
        super().__init__('Scissors')
