import datetime as dt
today = dt.date.today()
print(today)
print(today.month)
print(today.day)
print(today.year)

# If you have to print the specific date
new_year = dt.date(2024,1,1)    # format followed has to be YYYY/MM/DD
print(new_year)

daysleft = new_year - today
print(daysleft)