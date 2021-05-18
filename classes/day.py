class day:
    def __init__(self,conditionsObject):
        self.conditionsObject = conditionsObject
    rings = []
    dayNumber = 0
    def computed(self):
        computed = {}
        computed['fillRings'] = this.rings.count
        computed['emptyRings'] = self.conditionsObject.ringsConditions.rignsPerDay - this.rings.count
        return computed
