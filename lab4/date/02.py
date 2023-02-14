import datetime

tod = datetime.datetime.now()
y = tod - datetime.timedelta(days = 1)
tom = tod + datetime.timedelta(days = 1)

print("Yesterday", y.strftime("%d-%m-%Y"))

print("Today", tod.strftime("%d-%m-%Y"))

print("Tomorrow", tom.strftime("%d-%m-%Y"))