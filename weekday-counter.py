#import calendar module
import calendar

# this function counts the number of the given weekdays in the specific month of the specific year
def countdays (year, month, day):
   month = calendar.monthcalendar(year, month)
   count = 0
   for week in month:
      if week[day] != 0:
         count += 1
   return count

#initialising string to use later
daystr = ""

while (daystr != "exit"):
   try:   
      #show menu
      print("Enter 0 for Monday")
      print("Enter 1 for Monday")
      print("Enter 2 for Monday")
      print("Enter 3 for Monday")
      print("Enter 4 for Monday")
      print("Enter 5 for Monday")
      print("Enter 6 for Monday")
      print("Enter \"exit\" to quit the program")
      daystr = input("Enter weekday ").lower
      day = int(daystr)
      monthstr = input("Enter month ")
      month = int(monthstr)
      yearstr = input("Enter year ")
      year = int(yearstr)
   except Exception as e:
      if (daystr != "exit"):
         #if error print message
         print("invalid input")
      continue # skip to next interation in case of error
   finally:
      #error handling
      if (day > 6):
         print("Weekday must be between 0 and 6")
         continue
      elif (month > 12):
         print("Month must be between 0 and 12")
         continue
      #exit message
      elif daystr == "exit":
         print("goodbye")
      # returning result
      else:
         print("The number of days are" , countdays(year, month, day))



