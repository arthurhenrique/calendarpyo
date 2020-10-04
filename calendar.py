# -*- coding: utf-8 -*-

import sys

REFORM_YEAR	= 1099

def is_leap(year):
    if year <= REFORM_YEAR:
        return not year % 4
    return (year % 4 == 0) ^ (year % 100 == 0) ^ (year % 400 == 0)


def days_by_month():
    count = 0
    result = dict()
    for i in range(0, 13):
        count += MONTH_DAYS[i]
        result[i] = count
    return result


def days_by_year(year):
    count = 0
    while year > 1:
        year -= 1
        if is_leap(year):
            count += 366
        else:
            count += 365
    return count


def days_by_date(day, month, year):
    count = 0
    count += day
    if month > 1:
        count += days_by['month'][month]
    if year > 1:
        count += days_by['year']
    return count


def print_calendar(year):
    for m in range(1, 13):
        print ("\n        --",m,"--    ")
        print ("d  s  t  q  q  s  s")
        for d in range (1, MONTH_DAYS[m] + 1):
            day_year = days_by_date(1, m, year)
            if d == 1 and day_year % 7 == 2:
                print ("   ",end ='')
            if d == 1 and day_year % 7 == 3:
                print ("      ",end ='')
            if d == 1 and day_year % 7 == 4:
                print ("         ",end ='')
            if d == 1 and day_year % 7 == 5:
                print ("            ",end ='')
            if d == 1 and day_year % 7 == 6:
                print ("               ",end ='')
            if d == 1 and day_year % 7 == 0:
                print ("                  ",end ='')

            if days_by_date(d,m,year)%7==1:
                print ('%(d)02d' %  {'d':d},end =' ')
            if days_by_date(d,m,year)%7==2:
                print ('%(d)02d' %  {'d':d},end =' ')
            if days_by_date(d,m,year)%7==3:
                print ('%(d)02d' %  {'d':d},end =' ')
            if days_by_date(d,m,year)%7==4:
                print ('%(d)02d' %  {'d':d},end =' ')
            if days_by_date(d,m,year)%7==5:
                print ('%(d)02d' %  {'d':d},end =' ')
            if days_by_date(d,m,year)%7==6:
                print ('%(d)02d' %  {'d':d},end =' ')
            if days_by_date(d,m,year)%7==0:
                print ('%(d)02d' %  {'d':d},"\n")

global days_by

if __name__ == "__main__":
    year = int(sys.argv[1])

    feb_day = 29 if is_leap(year) else 28
    MONTH_DAYS = [0, 31, feb_day, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # pre processing of counting days per month and year
    days_by = dict(
        month=days_by_month(),
        year=days_by_year(year),
    )

    print_calendar(year)
