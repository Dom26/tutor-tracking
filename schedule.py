#This file contains the Schedule object that every tutor will have
#Each Schedule object contains one day and one timeframe

#Stuff to always run, such as classes and defs go outside the if __name__ == "__main__" statement
#print(__name__) 
# -Confirmed that __name__ == "__main__" when this file is executed
# -Confirmed that __name__ == "schedule" when called by the import statement from tutors.py
    
class Schedule:
    #day: a string representing one of the weekdays
    #time: a string representing a range of time ex: "12:00pm-4:00pm"
    def __init__(self, day = None, time = None):
        if day is None:
            self.day = ""
        else:
            self.day = day
        if time is None:
            self.time = ""
        else:
            self.time = time

        #Prints the day and time values for the Schedule object
        #This print method will be used when searching for individual tutors' schedules
    def printSchedule(self):
        print(self.day,self.time)

        #Prints only the time value of the Schedule's object
        #This print method will be used when searching for subjects and corresponding
        #tutors, and when printing the full tutor schedule
    def printTime(self):
        print(self.time)

        #prints the old day value, changes the value, then prints the new passed in
        #day value
    def changeDay(self, newDay):
        print("Previous day value: " + self.day)
        self.day = newDay
        print("Updated day value: " + self.day)

        #prints the old time frame, changes the time frame, then prints the updated
        #time frame
    def changeTime(self, newTime):
        print("Previous time frame: " + self.time)
        self.time = newTime
        print("Updated time frame: " + self.time)

        #method to change both the day and time, this method just calls the changeDay(day)
        #and changeTime(time) methods. This is the mehtod that'll be called when updating
        #schedules
    def changeSchedule(self,newDay,newTime):
        self.changeDay(newDay)
        self.changeTime(newTime)

    #Changes the day value to the empty string
    #used for when the schedule needs to be changed
    def clearDay(self):
        self.day = ""

    #Changes the time value to the empty string
    #used for when the schedule needs to be changed
    def clearTime(self):
        self.time = ""

#Testing that the Schedule object works as expected
if __name__ == "__main__":
    #Stuff to run when not called via an import statement
    s1 = Schedule("monday", "10:00am-1:00pm")

    s1.printSchedule()
    s1.printTime()

    print("Changing the day and time\n")
    s1.changeDay("tuesday")
    s1.changeTime("12:00pm-3:00pm")
    s1.printTime()
    s1.printSchedule()

    print("Using changeSchedule() method to update day and time\n")
    s1.changeSchedule("Friday","3:00pm-6:00pm")
    s1.printSchedule()
    s2 = Schedule()
    print("Printing an empty Schedule object. Nothing should print to screen:\n")
    s2.printSchedule()
    
    print("Adding day and time to empty Schedule object:\n")
    s2.changeSchedule("saturday","10:00am-2:00pm")

    print("Printing the new values of the previously empty Schedule object:\n")
    s2.printSchedule()
    print(s2.day,"+",s2.time,"+")
