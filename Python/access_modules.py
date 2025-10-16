import sys

locations=sys.path
print(locations)
for i in locations:
    print(i)

import calendar

leap_years = calendar.leapdays(2000,2024)

isitleap = calendar.isleap(2005)

print(leap_years)
print(isitleap)