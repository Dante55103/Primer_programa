import datetime

year = int(input("¿Que año es?: "))
month = int(input("¿Que mes es?: "))
day = int(input("¿Que día es?: "))

user_date = datetime.datetime(year=year, month=month, day=day)

time_remaining = user_date - datetime.datetime.now()

print("Faltan {} dias y {} horas.".format(time_remaining.days, int(time_remaining.seconds / 60 / 60 )))
print("Mañana es {}".format(datetime.datetime.now() + datetime.timedelta(days=1)))
print()