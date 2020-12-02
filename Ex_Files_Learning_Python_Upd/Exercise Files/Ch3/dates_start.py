#
# Example file for working with date information
#
from datetime import date
from datetime import datetime
from datetime import time

def main():
  ## DATE OBJECTS
  today = date.today()
  print(today)
  # Get today's date from the simple today() method from the date class
  print(today.day)
  print(today.month)
  print(today.year)

  # print out the date's individual components
  print(today.weekday())


  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  today = datetime.now()
  print(today.time())
  ## DATETIME OBJECTS
  # Get today's date from the datetime class

  
  # Get the current time

 

  
if __name__ == "__main__":
  main();
  