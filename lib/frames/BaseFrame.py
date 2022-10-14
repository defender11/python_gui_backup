class BaseFrame:
    def __init__(self, window, config):
        self.window = window
        self.config = config
        self.name = self.__class__
