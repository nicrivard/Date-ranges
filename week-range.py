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

# last week

lastStart = today - timedelta(days=7) - timedelta(days=today.weekday())
lastEnd = lastStart + timedelta(days=6)

print(str(lastStart.strftime("%y%m%d")) + " - " + str(lastEnd.strftime("%y%m%d")))

# days this week

Monday = today - timedelta(days=today.weekday())
Tuesday = Monday + timedelta(days=1)
Wednesday = Monday + timedelta(days=2)
Thursday = Monday + timedelta(days=3)
Friday = Monday + timedelta(days=4)
Saturday = Monday + timedelta(days=5)
Sunday = Monday + timedelta(days=6)

print("[[" + str(Monday.strftime("%y%m%d %A")) + "]]" + "\n" + "[[" + Tuesday.strftime("%y%m%d %A") + "]]" + "\n" + "[[" + Wednesday.strftime("%y%m%d %A") + "]]" + "\n"+ "[[" + Thursday.strftime("%y%m%d %A") + "]]" + "\n" + "[[" + Friday.strftime("%y%m%d %A") + "]]")
