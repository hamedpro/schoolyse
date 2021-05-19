def dayNumberToDayName(self,dayNumber):
    strings = [
        "saturday",
        "sunday",
        "monday",
        "thuesday",
        "wednesday",
        "thursday",
        "friday"
        ]
    return strings[dayNumber-1]  
def countEachItem(array):
    results = {}
    for i in range(len(array)):
        if results.__contains__(array[i]):
            results[array[i]] += 1
        else:
            results[array[i]] = 1
    return results
class day:
    rings = []
    ringNames = []
    dayNumber = None
    def analyse(self):
        for ring in self.rings:
            self.ringNames.append(ring.name)
        
        self.lessonsCount = common.countEachItem(self.ringNames)
class ring:
    durationInMinutes = 90
    def computed(self):
        computed = {}
        computed['test'] = self.durationInMinutes
        return computed

class school:
    def __init__(self,conditionsObject):
        self.conditionsObject = conditionsObject
    classRooms = []
    def computed(self):
        computed = {}
        computed['test'] = self.durationInMinutes
        return computed
class week:
    def __init__(self,conditionsObject):
        self.conditionsObject = conditionsObject
    days = []
    def computed(self):
        computed = {}
        computed['test'] = self.durationInMinutes
        return computed
