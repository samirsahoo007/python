import datetime
def get_time():
    current_date = datetime.datetime.now()
    hour = str(current_date.hour)
    minute = str(current_date.minute)

    return hour + minute

print(get_time())


