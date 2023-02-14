import datetime

today = datetime.datetime.now()
fda = today - datetime.timedelta(days=5)

print("Today :", today.strftime("%d/%m/%Y"))
print("Before five days :", fda.strftime("%d/%m/%Y"))