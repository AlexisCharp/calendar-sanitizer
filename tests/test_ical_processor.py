import unittest
from sanitizer.ical_processor import ICALProcessor

class TestICALProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = ICALProcessor()
        self.sample_ics = 'tests/test_data/sample.ics'

    def test_parse_ics(self):
        events = self.processor.parse_ics(self.sample_ics)
        self.assertIsInstance(events, list)
        self.assertGreater(len(events), 0)

    def test_sanitize_event(self):
        raw_event = {
            'summary': 'Test Event',
            'location': 'Test Location',
            'start_time': '20250313T093000Z',
            'end_time': '20250313T113000Z',
            'description': 'Test Description'
        }
        sanitized_event = self.processor.sanitize_event(raw_event)
        self.assertEqual(sanitized_event['summary'], 'Test Event')
        self.assertEqual(sanitized_event['location'], 'Test Location')
        self.assertIn('start', sanitized_event)
        self.assertIn('end', sanitized_event)

if __name__ == '__main__':
    unittest.main()