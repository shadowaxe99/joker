```python
from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class UserPreferences(Base):
    __tablename__ = 'user_preferences'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True, nullable=False)
    voice_selection = Column(String(50), nullable=False)
    script_customization = Column(String(500), nullable=True)
    call_schedule = Column(String(50), nullable=True)
    record_call = Column(Boolean, default=False)
    consent_given = Column(Boolean, default=False)

    def __init__(self, user_id, voice_selection, script_customization, call_schedule, record_call, consent_given):
        self.user_id = user_id
        self.voice_selection = voice_selection
        self.script_customization = script_customization
        self.call_schedule = call_schedule
        self.record_call = record_call
        self.consent_given = consent_given

def storeUserPreferences(user_id, voice_selection, script_customization, call_schedule, record_call, consent_given):
    user_preferences = UserPreferences(user_id, voice_selection, script_customization, call_schedule, record_call, consent_given)
    session.add(user_preferences)
    session.commit()
```