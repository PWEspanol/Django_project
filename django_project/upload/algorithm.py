import csv
import numpy as np
import pandas as pd
import math


# Checking distance between 2 coordinates in gps location

def gps_distance_between_coordinates(place_1, place_2):

    lat1, lon1 = place_1
    lat2, lon2 = place_2
    radius = 6371  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = radius * c

    
    return distance

# In ordedr to calculating maximum distance between 2
#  places for a plane i have to mutiply time
#  and plane's velocity

def searching_anomalies(filename):

    df = pd.read_csv(filename)

    for i in range(0,len(df.timestamp)-1):
        FlightTime = df.timestamp[i+1] - df.timestamp[i]
        
        MaximumPlaneDistance = (df.timestamp[i+1] - df.timestamp[i])/3600 * 950
        
        place_1 = [df.latitude[i], df.longitude[i]]
        place_2 = [df.latitude[i+1], df.longitude[i+1]]
        
        DistanceBetween2Coordinates = gps_distance_between_coordinates(place_1, place_2)
        
    
        if DistanceBetween2Coordinates >= MaximumPlaneDistance:
            index = i + 1
            df = df.drop(i+1)
    
    return df.to_csv()