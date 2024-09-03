from datetime import datetime

monthNameToNumberConverter = {
    "Jan" : "01",
    "Feb" : "02",
    "Mar" : "03",
    "Apr" : "04",
    "May" : "05",
    "Jun" : "06",
    "Jul" : "07", 
    "Aug" : "08",
    "Sep" : "09",
    "Oct" : "10", 
    "Nov" : "11", 
    "Dec" : "12"
}

def convertDateToDatetimeFormat(date:str) -> datetime:
    targetDate = date[:2] + "-" + monthNameToNumberConverter[date[3:5]] + "-" + date[6:]
    dateFormat = "%d-%m-%Y"
    targetDateTime = datetime.strptime(targetDate, dateFormat)
    return targetDateTime

def computeDelta(targetDay, sourceDay):
    if(targetDay > sourceDay):
        return 1
    elif (targetDay == sourceDay):
        return 0
    else:
        return -1

def dateDifferenceInMonths(sourceDate, targetDate):
    numericSourceDateTime = convertDateToDatetimeFormat(sourceDate)
    numericTargetDateTime = convertDateToDatetimeFormat(targetDate)

    return (numericTargetDateTime.year - numericSourceDateTime.year)*12 + (numericTargetDateTime.month - numericSourceDateTime.month) + computeDelta(numericTargetDateTime.day, numericSourceDateTime.day)

def compareDates(sourceDate, targetDate):
    sourceDateTime = convertDateToDatetimeFormat(sourceDate)
    targetDateTime = convertDateToDatetimeFormat(targetDate)
    return sourceDateTime < targetDateTime
