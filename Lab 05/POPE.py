def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
        else:
            return True
    else:
        return False

date = input("Please enter a date in MM/DD/YYYY format")
Month = int(date[0:2])
Day = int(date[3:5])
Year = int(date[6:10])

if Month in [4, 6, 9 ,11] : # month that has 30 days
    if Day >= 1 and Day <= 30:
        print('valid date')
    else:
        print('invalid day')
    print("30 day month")
    
elif Month in [1,3,5,7,8,10,12] : # month that has 31 days
    if Day <= 1 and Day <= 30:
        print('valid date')
    else:
        print('invalid day')
        
elif Month == 2: # month is February
        if Day >= 1 and Day <= 28:
            print('valid date')
        elif Day == 29:
            if isLeapYear(Year):
                print('valiid day')
            else:
                print('iinvalid day, noot a leap year')
        else:
            print('invalid day')


