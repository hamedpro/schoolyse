class classRoom:
    def __init__(self,conditionsObject):
        self.conditionsObject = conditionsObject
    days = []
    def computed(self):
        computed = {}
        computed['test'] = self.durationInMinutes
        return computed
