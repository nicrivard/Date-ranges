from datetime import datetime, timedelta
today = datetime.now().date()

# this week

start = today - timedelta(days=today.weekday())
end = start + timedelta(days=6)

print(str(start.strftime("%y%m%d")) + " - " + str(end.strftime("%y%m%d")))

# next week

nextStart = today + timedelta(days=7) - timedelta(days=today.weekday())
nextEnd = nextStart + timedelta(days=6)

print(str(nextStart.strftime("%y%m%d")) + " - " + str(nextEnd.strftime("%y%m%d")))
