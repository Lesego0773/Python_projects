#!/bin/bash/python3

from fastapi import FastAPI
from app.api_fetcher import fetch_flight_data
from app.analyzer import analyze_flights
from app.database import init_db

app = FastAPI()

#Initializing the database when the app starts
@app.on_event("startup")
def on_startup():
    init_db()

#Endpoint to fetch and analyze flight data
@app.get("/flights")
def get_flights():
    data = fetch_flight_data() #Getting flight data from API
    analysis = analyze_flights(data) #analyzing altitude and speed

    return {
        "sample_size": data[:10], #Returning first 10 records for brevity
        "analysis": analysis, #Including summary statistics
    }
