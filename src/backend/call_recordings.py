```python
from sqlalchemy import Column, Integer, String, DateTime
from database import Base, session

class RecordingSchema(Base):
    __tablename__ = 'callRecordings'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    call_id = Column(Integer)
    recording_file = Column(String)
    timestamp = Column(DateTime)

def storeCallRecording(user_id, call_id, recording_file, timestamp):
    new_recording = RecordingSchema(user_id=user_id, call_id=call_id, recording_file=recording_file, timestamp=timestamp)
    session.add(new_recording)
    session.commit()

def getCallRecording(call_id):
    recording = session.query(RecordingSchema).filter_by(call_id=call_id).first()
    return recording

def getAllRecordings(user_id):
    recordings = session.query(RecordingSchema).filter_by(user_id=user_id).all()
    return recordings
```