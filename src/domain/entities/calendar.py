from datetime import datetime
from typing import List, Optional
from .user import User
from .activity import Activity

class Calendar():
    def __init__(self, owner:User):
        self.owner = owner
    
    def _slot_free(self, activity:Activity):
        for an_activity in self.owner.today_activities():
            if an_activity.conflicts(activity):
                return False
        return True

    def add_activity(self, activity:Activity):
        if self._slot_free(activity):
            activity.create()
    