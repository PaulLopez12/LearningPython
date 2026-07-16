### Dates ###

# Date time

from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime

now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())
    
print_date(now)

year_2026 = datetime(2026,7,12)

print_date(year_2026)
print("--------------------------")

# Time
current_time = time(18,21,19)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)
print("--------------------------")

# Date 
current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2026,7,12)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month, current_date.day)
print(current_date.month)
print("--------------------------")

# Operaciones con fechas

diff = year_2026.date() - current_date
print(diff)
print("--------------------------")

# Timedelta
start_timedelta = timedelta(200,100,100,weeks=10)
end_timedelta = timedelta(300,100,100,weeks=13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)