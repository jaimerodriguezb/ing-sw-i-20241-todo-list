from datetime import datetime
from typing import List, Optional

from ..value_objects import ActivityId

class Activity():
    def __init__(self, id=None, name=None, user=None, hour=None, date=None):
        super().__init__()
        self.acti_id = id
        self.acti_name = name
        self.acti_hour = hour
        self.acti_date = date
        if user:
            self.user_id = user.user_id

