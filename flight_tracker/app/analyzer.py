!#/bin/bash/python3


#Analyzing flight data to compute statistics
def analyze_flights(flight_data):

    #Extracting all altitudes (index 7) that are not None
    altitudes = [state[7] for state in flight_data if state[7] is not None]


    #Handling the case where no altitude data is available
    if not altitudes:
        return {
            "average_altitude": 0,
            "high_altitude_count": 0,
        }

    #Calculating the avaerage altitude
    avg_alt = sum(altitudes) / len(altitudes)

    #Count number of flights above 40, 000 feet
    high_altitude_flights = [state for state in flight_data if state[7] is not None and state[7] > 40000]

    return {
        "average_altitude": round(avg_alt, 2),
        "high_altitude_count": len(high_altitude_flights),
    }


