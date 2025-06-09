import os
from sanitizer.ical_processor import ICALProcessor

def main():
    ics_file_path = os.path.join(os.path.dirname(__file__), 'data', 'ADECal.ics')
    processor = ICALProcessor()
    sanitized_events = processor.parse_ics(ics_file_path)

    for event in sanitized_events:
        print(event)

if __name__ == "__main__":
    main()