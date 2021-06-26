def countEachItem(array):
    results = {}
    for i in range(len(array)):
        if results.__contains__(array[i]):
            results[array[i]] += 1
        else:
            results[array[i]] = 1
    return results    
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
for i in results:
    print(i)




