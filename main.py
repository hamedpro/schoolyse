class convertor:
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

class dataCollectedFromUser:
    eachDayRingsCount = None 
    eachWeekDaysCount = None
    eachSchoolWeeksCount = None

class ring:
    durationInMinutes = 90
    def analyse(self):
        pass
class day:
    rings = []
    ringNames = []
    dayNumber = None
    def analyse(self):
        for ring in self.rings:
            self.ringNames.append(ring.name)
        self.lessonsCount = common.countEachItem(self.ringNames)
class week:
    days = []
    def analyse(self):
        pass 
class school:
    classRooms = []
    def analyse(self):
        pass

class conditions:
    conditionCodes = []
    def verifyConditions(school):
        for conditionCode in self.conditionCodes:
            if conditionCode == 1:
                pass
            if conditionCode == 2:
                pass

class ringPointer:
    def __init__(self,d:dataCollectedFromUser):
        self.dataCollectedFromUser = d
    focusedRing = [0,0,0] #3d array and is pointing to [weekIndex,dayIndex,ringIndex]
    def goToNextRing(self):
        if self.focusedRing[2]+1 <= self.dataCollectedFromUser.eachDayRingsCount -1 :
            self.focusedRing[2] += 1
            return True
        else:
            self.focusedRing[2] = 0
            if self.focusedRing[1]+1 <= self.dataCollectedFromUser.eachWeekDaysCount -1:
                self.focusedRing[1] += 1
                return True
            else:
                self.focusedRing[1] = 0
                if self.focusedRing[0]+1 <= self.dataCollectedFromUser.eachSchoolWeeksCount -1:
                    self.focusedRing[0] += 1
                    return True
                else:
                    self.focusedRing = [0,0,0]
