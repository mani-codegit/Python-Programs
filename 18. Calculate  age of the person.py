#Calculate the age of the person print their age in year
import datetime
year=int(input("Enter the year of born "))
month=int(input("Enter the month of born "))
date=int(input("Enter the date of born"))
now=datetime.datetime.now()
born=datetime.datetime(year,month,date)
ageyear=now.year-born.year
print(f"your age is {ageyear}")