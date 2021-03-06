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
        
class classRoom:
    days = []
    def analyse(self):
        for i in range(len(self.days)):
            self.days[i].analyse()
class school:
    classRooms = []
    def analyse(self):
        for i in range(len(self.classRooms)):
            self.classRooms[i].analyse()



def buildSchoolFromArray(array,RingsCount,daysCount,classRoomsCount):
    tmpDay = day()
    for i in range(RingsCount):
        tmpDay.rings.append(ring())
    tmpClassRoom = classRoom()
    for i in range(daysCount):
        classRoom.days.append(day())
    tmpSch = school()
    for i in range(classRoomsCount):
        tmpSch.classRooms.append(classRoom())
    return tmpSch

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
        
    for classRoom in school.classRooms:
        try:
            printWithIndent(classRoom.name,1)
        except:
            printWithIndent("[week name]",1)
        for day in classRoom.days:
            try:
                printWithIndent(day.name,2)
            except:
                printWithIndent("[day name]",2)
            for ring in day.rings:
                try:
                    printWithIndent(ring.name,3)
                except:
                    printWithIndent("[ring name]",3)


lessons = ["farsi","english","lesson 3"]
results = []
maxlen = 3
def fill_next_cell(array):
    cloned = array.copy()
    if len(cloned) == maxlen:
        results.append(cloned)
    else:
        cloned.append(None)
        index_to_inject = len(cloned)-1
        for lesson in lessons:
            cloned[index_to_inject] = lesson
           
            fill_next_cell(cloned)

fill_next_cell([])





