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
