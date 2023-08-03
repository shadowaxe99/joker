import datetime

class CallScheduling:
    def __init__(self):
        self.scheduled_calls = []

    def schedule_call(self, call, date, time):
        scheduled_time = datetime.datetime.strptime(date + ' ' + time, '%Y-%m-%d %H:%M')
        self.scheduled_calls.append((call, scheduled_time))