#This file contains the Schedule object that every tutor will have
#Each Schedule object contains one day and one timeframe
class Schedule:
    def __init__(self, day, time):
        self.day = day
        self.time = time

#Prints the day and time values for the Schedule object
#This print method will be used when searching for individual tutors' schedules
    def printSchedule(self):
        print(self.day + "\t" + self.time)

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
