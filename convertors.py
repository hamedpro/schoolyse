from typing import AbstractSet
from schoolyse import day


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