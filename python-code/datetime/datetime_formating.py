from datetime import datetime

dt = datetime(2000, 10, 2, 0, 0, 0, 0)
print(dt)

# Prints datetime in iso8605 format 
print(dt.isoformat())

date_str = "01.02.2020"
time_str = "00:04:56,420"

datetime_str = date_str + " " + time_str
format_str = "%d.%m.%Y %H:%M:%S,%f"
dt = datetime.strptime(datetime_str, format_str)
print(dt.isoformat(timespec="milliseconds"))