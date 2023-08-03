import datetime

class PrankCallScheduler:
    def __init__(self):
        self.scheduled_calls = []

    def schedule_prank_call(self, prank_call, date, time):
        scheduled_time = datetime.datetime.strptime(date + ' ' + time, '%Y-%m-%d %H:%M')
        self.scheduled_calls.append((prank_call, scheduled_time))

    def cancel_scheduled_prank_call(self, prank_call):
        for scheduled_call in self.scheduled_calls:
            if scheduled_call[0] == prank_call:
                self.scheduled_calls.remove(scheduled_call)
                break