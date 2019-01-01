import calendar

#create calendar and start of the month is Sunday
c=calendar.TextCalendar(calendar.SUNDAY)
print(c.formatyear(2019))

days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
d=calendar.weekday(2019,1,3)
print(days[d])
