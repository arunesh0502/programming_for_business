import datetime

date_time_one = datetime.datetime(2026, 9, 14, 16, 30)
date_time_two = datetime.datetime(2026, 9, 15, 16, 30)

print(date_time_one.strftime("%A, %d %B %Y"))
print(date_time_two.strftime("%A, %d %B %Y"))

if date_time_one < date_time_two:
    print("The first time is earliest.")
elif date_time_two < date_time_one:
    print("The second time is earliest.")
else:
    print("The times are the same")