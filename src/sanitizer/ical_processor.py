import icalendar
from datetime import datetime
from models.event import Event

class ICALProcessor:
    def __init__(self, ics_file):
        self.ics_file = ics_file
        self.events = []

    def parse_ics(self):
        with open(self.ics_file, 'r') as file:
            calendar = icalendar.Calendar.from_ical(file.read())
            for component in calendar.walk():
                if component.name == "VEVENT":
                    event = self.sanitize_event(component)
                    if event:
                        self.events.append(event)

    def sanitize_event(self, component):
        summary = component.get('summary')
        location = component.get('location')
        start_time = component.get('dtstart').dt
        end_time = component.get('dtend').dt

        if isinstance(start_time, datetime) and isinstance(end_time, datetime):
            return Event(summary, location, start_time.isoformat(), end_time.isoformat())
        return None

    def convert_to_google_format(self):
        google_events = []
        for event in self.events:
            google_events.append({
                'summary': event.summary,
                'location': event.location,
                'start': {
                    'dateTime': event.start_time,
                    'timeZone': 'Europe/Paris',
                },
                'end': {
                    'dateTime': event.end_time,
                    'timeZone': 'Europe/Paris',
                },
            })
        return google_events