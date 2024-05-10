
class User():
    def __init__(self, name=None, last_name=None, email=None, activities=None, id=None):
        super().__init__()
        self.user_id = id
        self.user_name = name
        self.user_last_name = last_name
        self.user_email = email
        if activities:
            self.activities = sorted(activities, key=lambda activity: activity.acti_hour)

    def today_activities(self):
        return self.activities
