# XSS Test Application

A Flask-based web application for testing and demonstrating XSS vulnerabilities and security measures.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd xss1
```

2. Create and activate a virtual environment:

On macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
python app.py
```
This will create the SQLite database with some test users.

## Running the Application

1. Make sure your virtual environment is activated (see step 2 above)

2. Start the Flask development server:
```bash
python app.py
```

3. Access the application in your web browser at:
```
http://localhost:8070
```

## Features

- User authentication system
- Comment functionality
- URL fetching capability
- User search functionality
- Ping utility

## Security Features

- Content Security Policy (CSP) implementation
- SQL injection protection
- Command injection protection

## Note

This application is designed for educational purposes to demonstrate web security concepts. Some features may intentionally contain vulnerabilities for demonstration purposes.

