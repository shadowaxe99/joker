```python
import datetime
from src.backend.database import scheduledCalls

def scheduleCall(user_id, prank_id, schedule_time):
    """
    Function to schedule a prank call.
    """
    # Validate the schedule_time
    try:
        schedule_time = datetime.datetime.strptime(schedule_time, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return {"status": "error", "message": "Invalid date/time format. Please use 'YYYY-MM-DD HH:MM:SS' format."}

    # Check if the schedule_time is in the future
    if schedule_time <= datetime.datetime.now():
        return {"status": "error", "message": "Schedule time must be in the future."}

    # Add the prank call to the scheduledCalls
    scheduledCalls.append({
        "user_id": user_id,
        "prank_id": prank_id,
        "schedule_time": schedule_time
    })

    return {"status": "success", "message": "Prank call scheduled successfully."}
```