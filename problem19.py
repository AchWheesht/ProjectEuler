# You are given the following information, but you may prefer to do some research for yourself.
#
#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


#In a given year...

days_in_year = (31*7) + (30*4) + 28
days_in_year = 365
one_hundred_years = 365000
twenty_four_leap_days = 365024

total_days = 36524

months = [
    "jan",
    "feb",
    "mar",
    "apr",
    "may",
    "jun",
    "jul",
    "aug",
    "sep",
    "oct",
    "nov",
    "dec"
    ]

def leap_year():
    if year % 4 == 0 and year % 100 != 0:
        return 29
    else:
        return 28

days_in_month = {
    "jan": 31,
    "feb": 28,
    "mar": 31,
    "apr": 30,
    "may": 31,
    "jun": 30,
    "jul": 31,
    "aug": 31,
    "sep": 30,
    "oct": 31,
    "nov": 30,
    "dec": 31
}

day = 1
month = months[0]
month_count = 0
day_limit = days_in_month[month]
day_of_week = 1
year = 1
count = 0

for i in range (1, total_days):
    print(day, month, year)
    if day == 1 and day_of_week == 7:
        count += 1
    day += 1
    if day > day_limit:
        day = 1
        month_count += 1
        try:
            month = months[month_count]
        except IndexError:
            month_count = 0
            year += 1
            month = months[month_count]
        day_limit = days_in_month[month]
        if month_count == 1:
            if year % 4 == 0 and year % 100 != 0:
                day_limit += 1
        day_of_week += 1
        if day_of_week > 7: day_of_week = 1

print(day, month, year)
print(count)
