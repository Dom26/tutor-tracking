#This file contains the tutors objects
#Each tutor will have a name, and an array of Schedule objects
#I'm thinking of making it a 2D array with 7 columns and starts
#with 1 row initially, but a new row can be added if there are
#multiple shifts in a day.
#Maybe an array of lists would work out better so that I wouldn't
#have to remake the entire array and copy contents over when I want
#to add a new day/time shift, but iterating through the array of lists
#might be more of a pain.
#I'll try the 2D array approach and see what happens

import schedule

# weekdays represent the 7 days of the week
weekdays = 7
daysOfTheWeek = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

#Use this function to find the correct day of the week the user sent
def findDay(day):
    num = 0
    while daysOfTheWeek[num] != day:
        num = num + 1
    return num

#Use this function to return a string with the correct number of whitespaces
#for proper alignment
#The smallest timeframe string is 13 characters, meaning the timeframe lengths will always be
#longer than the days lengths
#Formula to find the amount of space from the end of the timeframe string to the next weekday for 
#proper spacing:
#20 - (len(time) - len(day)) if day/time != ""
#20 + len(daysOfWeek[x]) if day/time == ""
# that calculated value is used to pad the the time string with whitespaces so the next time value
#properly aligns with the next weekday
#length of an empty string "" is zero
def spacePadding(timeStrLen,dayNum):
    #args:
    #   timeStrLen: The length of the timeframe
    #   dayNum: The number in the daysOfWeek array
    padding = ""
    dayLen = len(daysOfTheWeek[dayNum])
    padNum = 0
    
    if timeStrLen == 0:
        padNum = 20 + dayLen
    else:
        padNum = 20 - (timeStrLen - dayLen)

    i = 0
    #Might need to use <= rather than <
    while i < padNum:
        padding = padding + " "
        i = i + 1

    return padding

class Tutor:
    #numOfShifts:   Represents the maximum number of shifts a tutor works on one of the weekdays
    #tutorName:     The tutor's name
    #shiftSchedule: A 2D array where each row is an array of schedule object and each
    #               column is a day of the week
    #toDelete:      Tells the program to show the Tutor's data, and whether or not to save the data
    #               It's good to note that the data won't actually be deleted, just ignored until
    #               the program saves the data to a file, where upon restarting the Tutor's data will
    #               no longer be present
    def __init__(self,tutorName,day,time):
        self.numOfShifts = 1
        self.tutorName = tutorName
        self.shiftSchedule = [[schedule.Schedule() for i in range(weekdays)] for j in range(self.numOfShifts)]
        num = findDay(day)
        self.shiftSchedule[0][num].day = day
        self.shiftSchedule[0][num].time = time
        self.toDelete = False

    #changes the name of the tutor to the passed in string
    def changeTutorName(self,newName):
        self.tutorName = newName

    #Returns the Tutor object's tutorName string
    def getTutorName(self):
        return self.tutorName

    #Changes the toDelete value to true in order to exclude saving the information when
    #saving the tutor's data
    def deleteTutor(self):
        self.toDelete = True

    #Returns the toDelete value to the caller
    def tutorDeleted(self):
        return self.toDelete

    #prints the day and time for tutors shifts
    #each row is a list of schedule objects
    #The 2nd loop iterates through that list looking for nonempty
    #Schedule objects
    def printTutor(self):
        print(self.tutorName)
        for row in self.shiftSchedule:
            for i in range(weekdays):
                if row[i].day == "":
                    continue
                row[i].printSchedule()

    #Updates the shiftSchedule 2D array to have 1 more row of Schedule objects
    def addNewWeek(self):
        #Create a temporary 2D array that has one more row than the current object's 2D array
        incrShifts = self.numOfShifts + 1
        tempShift = [[schedule.Schedule() for i in range(weekdays)] for j in range(incrShifts)]
        #Go through the object's 2D array and copy the contents of that array into the tempory 2D array
        x = 0
        for row in self.shiftSchedule:
            for i in range(weekdays):
                tempShift[x][i].day = row[i].day
                tempShift[x][i].time = row[i].time
            x = x + 1
        #Create a new 2D array for shiftSchedule that's the same size as the temporary 2D array
        #copy the contents of the temporary array to the shiftSchedule
        self.shiftSchedule = [[schedule.Schedule() for t in range(weekdays)] for z in range(incrShifts)]
        x = 0
        for row2 in tempShift:
            for n in range(weekdays):
                self.shiftSchedule[x][n].day = row2[n].day
                self.shiftSchedule[x][n].time = row2[n].time
            x = x + 1
        self.numOfShifts = incrShifts

    #Looks thourgh the shiftSchedule 2D array to find the place to add the new day/time shift
    #If it can't find a spot with an empty day value, then it calls the addNewWeek() method
    def updateSchedule(self,day,time):
        num = findDay(day)
        #shift should start at zero and increase to numOfShifts looking for an empty spot
        #if it can't find an empty spot in the correct day then it makes a call to the
        #addNewWeek() method
        shift = 0
        while shift < self.numOfShifts:
            if self.shiftSchedule[shift][num].day == "":
                break
            shift = shift + 1

        if shift == self.numOfShifts:
            self.addNewWeek()

        self.shiftSchedule[shift][num].day = day
        self.shiftSchedule[shift][num].time = time
    
    #Returns the times that the tutor works as a formatted string
    def getShiftTimesAsString(self):
        formattedTimesString = "\t\t"
        
        for row in self.shiftSchedule:
            for i in range(weekdays):
                formattedTimesString = formattedTimesString + row[i].time
                if daysOfTheWeek[i] != "sunday":
                    formattedTimesString = formattedTimesString + spacePadding(len(row[i].time),i)
                else:
                    formattedTimesString = formattedTimesString + "\n\t\t"
        
        formattedTimesString = formattedTimesString + "\n"
        return formattedTimesString


if __name__ == "__main__":
    print("Creating a tutor object with initial schedule:")
    t1 = Tutor("Adam","monday","10:00am-12:00pm")
    t1.printTutor()

    print("Adding a new day/time to the tutor's schedule:")
    t1.updateSchedule("wednesday","10:00am-12:00pm")
    t1.printTutor()

    print("Adding a new shift to a day that has a time associated with it.")
    print("This should increase the number of rows in the 2D array by 1:")
    t1.updateSchedule("monday","12:30pm-2:30pm")
    t1.printTutor()

    print("Adding a new shift to another day that has a time associated with it.")
    print("This should not increase the number of rows in the 2D array, and should")
    print("not overwrite the time in the other shift spot:")
    t1.updateSchedule("wednesday","12:30pm-2:30pm")
    t1.printTutor()

    print("Adding a day/time that hasn't been added to Schedule 2D array yet.")
    print("2D array shouldn't change its size:")
    t1.updateSchedule("friday","10:00am-2:00pm")
    t1.printTutor()

    #someStr = "This is a string."
    #print(someStr)
    #someStr = someStr + "\nThis should be a newline in the same string."
    #print(someStr)

    schedString = "\t\t"
    #A tab is 8 whitespaces
    for i in range(len(daysOfTheWeek)):
        schedString = schedString + daysOfTheWeek[i]
        if daysOfTheWeek[i] == "sunday":
            schedString = schedString + "\n"
        else:
            schedString = schedString + "                    "
    #that's 20 spaces, tabs weren't giving uniform spacing
    #The smallest timeframe string is 13 characters, meaning the timeframe lengths will always be
    #longer than the days lengths
    #Formula to find the amount of space from the end of the timeframe string to the next weekday for 
    #proper spacing:
    #20 - (len(time) - len(day)) if day/time != ""
    #20 + len(daysOfWeek[x]) if day/time == ""
    # that calculated value is used to pad the the time string with whitespaces so the next time value
    #properly aligns with the next weekday
    print(schedString)
    print(t1.getShiftTimesAsString())
    t1.updateSchedule("tuesday","2:00pm-5:00pm")
    t1.updateSchedule("thursday","2:00pm-5:00pm")
    print(schedString)
    print(t1.getShiftTimesAsString())
    t1.updateSchedule("sunday","11:00am-1:30pm")
    print(schedString)
    print(t1.getShiftTimesAsString())
    t1.updateSchedule("sunday","2:00pm-3:00pm")
    print(schedString)
    print(t1.getShiftTimesAsString())
    t1.updateSchedule("sunday","3:30pm-6:00pm")
    print(schedString)
    print(t1.getShiftTimesAsString())
