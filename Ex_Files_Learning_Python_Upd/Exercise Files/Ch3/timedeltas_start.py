#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it

print(timedelta(days=10, hours=10, minutes=30))

# print today's date
now = datetime.now()
print("today's date: ", now.date())

# print today's date one year from now
print("one year from now: ", (now + timedelta(days=365)).date())


# create a timedelta that uses more than one argument


# calculate the date 1 week ago, formatted as a string


### How many days until April Fools' Day?


# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year


# Now calculate the amount of time until April Fool's Day  

