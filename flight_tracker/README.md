# Real-Time Flight Tracker & Analyzer

A web-based app to monitor real-time aircraft data using the OpenSky Network API.

## Features
- Live flight data fetching
- Altitude and speed analysis
- API endpoint to display data

## Run
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/flights` for data output.

