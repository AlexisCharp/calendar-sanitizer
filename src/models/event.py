class Event:
    def __init__(self, summary, location, start_time, end_time):
        self.summary = summary
        self.location = location
        self.start_time = start_time
        self.end_time = end_time

    def to_google_format(self):
        return {
            "summary": self.summary,
            "location": self.location,
            "start": {
                "dateTime": self.start_time,
                "timeZone": "Europe/Paris",
            },
            "end": {
                "dateTime": self.end_time,
                "timeZone": "Europe/Paris",
            },
        }