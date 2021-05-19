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
class ring:
    duration = 90
    def analyse(self):
        pass
class day:
    rings = [] # ring objects 
    ringNames = [] # name prop of ring objects 
    dayNumber = None
    def analyse(self):
        for ring in self.rings:
            self.ringNames.append(ring.name)
        for i in range(len(self.rings)):
            self.rings[i].analyse()
        self.lessonsCount = common.countEachItem(self.ringNames)
        self.dayName = myConvertor.dayNumberToDayName(self.dayNumber)
        
class week:
    days = []
    def analyse(self):
        for i in range(len(self.days)):
            self.days[i].analyse()
class school:
    weeks = []
    def analyse(self):
        for i in range(len(self.weeks)):
            self.weeks[i].analyse()

class conditionManager:
    eachDayRingsCount = None 
    eachWeekDaysCount = None
    eachSchoolWeeksCount = None
    lessonCountLimit = object()
    conditionToVerify = [] #it holds condition codes
    def analyse(self):
        #update computed props
        pass 
    def verifyConditions(self,school):
        for conditionCode in self.conditionCodes:
            if conditionCode == 1:
                pass
            if conditionCode == 2:
                pass

class ringPointer:
    def __init__(self,d:conditionManager):
        self.conditionManager = d
    focusedRing = [0,0,0] #3d array and is pointing to [weekIndex,dayIndex,ringIndex]
    def goToNextRing(self):
        if self.focusedRing[2]+1 <= self.conditionManager.eachDayRingsCount -1 :
            self.focusedRing[2] += 1
            return True
        else:
            self.focusedRing[2] = 0
            if self.focusedRing[1]+1 <= self.conditionManager.eachWeekDaysCount -1:
                self.focusedRing[1] += 1
                return True
            else:
                self.focusedRing[1] = 0
                if self.focusedRing[0]+1 <= self.conditionManager.eachSchoolWeeksCount -1:
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
class schoolyse:
    ringPointer = None
    conditionManager = None
    school = None
    def fillRing(self):
        for lesson in self.conditionManager.lessons:
            ringLoc = self.ringPointer.focusedRing()
            school.weeks[ringLoc[0]].days[ringLoc[1]].rings[ringLoc[2]].name = lesson
            school.analyse()
            if self.conditionManager.verifyConditions(self.school)== True:
                self.fillRing()
    def startApp(self):
        fillRing() #todo this class methods









