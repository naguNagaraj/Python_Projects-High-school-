# i should create a python program which helps to enter the age and name and display it.
# def age():

#     b = input("Enter the name : ")
#     a = int(input("Enter the age : "))
#     z = a*12
#     c = z*31
#     print("The age of",b,"is",a,"or",z,"months old or",c,"days old.")
# age()


import time
from calendar import isleap


def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False

def month_days(month, leap_year):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month ==2 and (not leap_year):
        return 28
name = input("Enter your name : ")
age = int(input("Enter your age "))
localtime = time.localtime(time.time())


year = int(age)
month = year * 12 + localtime.tm_mon
day = 0 

begin_year = int(localtime.tm_year) - year
end_year = begin_year + year

for i in range(begin_year,end_year):
    if (judge_leap_year(i)):
        day = day + 366
    else:
        day = day = 365

learp_year = judge_leap_year(localtime.tm_year)

for m in range(1,localtime.tm_mon):
    day = day + month_days(m, learp_year)

day = day + localtime.tm_mday
print("%s' age is %d years or "%(name,year), end = "")
print("%d months or %d days" %(month,day))
