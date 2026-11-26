# PulseWatch — DevOps Website Monitoring System

PulseWatch is a beginner-friendly website monitoring web app. It checks a publicly reachable website and displays its HTTP status code, availability, and response time.

## Features
- Check public website availability
- Display HTTP status code
- Measure response time
- Simple web interface
- Health endpoint for basic app health checks
- Automated tests with pytest
- CI workflow using GitHub Actions
- Docker container setup

## Technology Stack
Python, Flask, Requests, pytest, Git, GitHub Actions, Docker

## Run locally
1. Install Python 3.10+.
2. Clone this repository.
3. Create and activate a virtual environment.
4. Install dependencies: `pip install -r requirements.txt`
5. Start the app: `python app.py`
6. Open `http://localhost:5000`

## Run tests
`pytest -q`

## Docker
Build: `docker build -t pulsewatch .`
Run: `docker run --rm -p 5000:5000 pulsewatch`
Then open `http://localhost:5000`.

## Git workflow
See [branches.md](branches.md).

## Internship
SWYNEX Technologies — DevOps Internship project.
