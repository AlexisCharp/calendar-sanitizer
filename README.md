# README.md

# Calendar Sanitizer

The Calendar Sanitizer is a Python application designed to read and sanitize event data from .ics files, transforming it into a format suitable for Google Calendar import. This project aims to streamline the process of importing calendar events by ensuring that the data is clean and correctly formatted.

## Features

- Parse .ics files to extract event data.
- Sanitize event details to remove any unwanted characters or formatting.
- Convert events into a Google Calendar-compatible format.

## Installation

To get started with the Calendar Sanitizer, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd calendar-sanitizer
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:

```
python src/main.py
```

Make sure to place your .ics file in the appropriate directory or modify the script to point to the correct file path.

## Testing

To run the tests for the Calendar Sanitizer, use the following command:

```
pytest
```

This will execute the unit tests defined in the `tests` directory.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.