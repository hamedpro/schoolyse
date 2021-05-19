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
myConvertor = convertor()
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
    lessonCountLimit = object()
    def analyse(self):
        self.eachWeekRingsCount = self.eachWeekDaysCount * self.eachDayRingsCount

class ring:
    durationInMinutes = 90
    def analyse(self):
        pass
class day:
    rings = [] # ring objects 
    ringNames = [] # name prop of ring objects 
    dayNumber = None
    def analyse(self):
        for ring in self.rings:
            self.ringNames.append(ring.name)
        self.lessonsCount = common.countEachItem(self.ringNames)
        self.dayName = myConvertor.dayNumberToDayName(self.dayNumber)
        
class week:
    days = []
    def analyse(self):
        pass 
class school:
    weeks = []
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
def schoolBuilder(weeksCount,daysCount,ringsCount):
    result = school()
    d = day()
    for i in range(ringsCount):
        day.rings.append(ring)
    w = week()
    for i in range(daysCount):
        w.days.append(d)
    for i in range(weeksCount):
        result.weeks.append(w)
    return result

    
def printWithIndent(string,indentCount):
    modifiedString = ""
    for i in range(indentCount):
        modifiedString += " " * 3
    modifiedString += string
    print(modifiedString)
def printSchool(school):
    try:
        print(school.name)
    except:
        print("[school name]")
        
    for week in school.weeks:
        try:
            printWithIndent(week.name,1)
        except:
            printWithIndent("[week name]",1)
        for day in week.days:
            try:
                printWithIndent(day.name,2)
            except:
                printWithIndent("[day name]",2)
            for ring in day.rings:
                try:
                    printWithIndent(ring.name,3)
                except:
                    printWithIndent("[ring name]",3)
s = schoolBuilder(3,4,5)
printSchool(s)
