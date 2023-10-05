class ManagerHandler:
    def __init__(self, manager=None):
        self.manager = manager

    def set_manager(self, manager):
        self.manager = manager

    def get_manager(self):
        return self.manager
