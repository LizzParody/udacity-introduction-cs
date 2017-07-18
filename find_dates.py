def nextDay(year, month, day):
    if day < 30:
        return year, month, day + 1
    elif month == 12:
        return year + 1, 1, 1
    else:
        return year, month + 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if(year1 < year2):
        return True
    elif(year1 == year2):
        if(month1 < month2):
            return True
        elif(month1 == month2):
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = 0
    while(dateIsBefore(year1, month1, day1, year2, month2, day2)):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def test():
    test_cases = [((2012,9,30,2012,10,30),30),
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
