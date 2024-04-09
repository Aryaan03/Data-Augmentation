import re
import argparse
import pypdf
import urllib.request
import sqlite3
import io
import requests
import requests_cache
import math
import time
import pandas as pd
from geopy.geocoders import Nominatim
from datetime import datetime
from collections import Counter
import openmeteo_requests
from retry_requests import retry
import tabulate

## Import All the necessary Packages

def RetrieveIncidents(url):
# Function to Retive incident data from the given URL
    headers = {
        # Initialize headers to mimic user agent
        'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    }
    # Open the URL with the provided headers and request to read the data
    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
    #Opening URL for requesting to read the data
    return data

def ExractData(IncidentData):
# Function to extract incidents from PDF file

    # Read PDF data from BytesIO object
    ReadPDF = pypdf.PdfReader(io.BytesIO(IncidentData))
    # Initialize empty string to store extracted text
    ExtractText = ""

    # Iterate through every page in PDF file
    for PageNo in range(len(ReadPDF.pages)):
        # Add a new line before each page's text
        ExtractText += "\n"
        page = ReadPDF.pages[PageNo]

        # Extracting text from the page
        page_text = page.extract_text(extraction_mode="layout")
        #Appending the result with the extracted text
        ExtractText += page_text
        # print(ExtractText)
   
    # Return the extracted text
    return ExtractText
        

def DataBase(Norman, Tab, Info):
    # Function to create SQLite database and populate it with incident data
    y = sqlite3.connect(Norman)
    # Connect to SQLite database
    x = y.cursor()
    ## Create a cursor object

    x.execute("DROP TABLE IF EXISTS {};".format(Tab))
    # Drop table if already exists

    Qur = """
        CREATE TABLE {} (Incident_Time TEXT, Incident_Number TEXT, Incident_Location TEXT, Nature TEXT, Incident_ori TEXT, 
            Day_of_the_Week INTEGER, Time_of_day INTEGER, Weather INTEGER, Location_Rank INTEGER,Side_of_Town TEXT,
            Incident_Rank INTEGER, Nat TEXT, EMSSTAT INTEGER);""".format(Tab)
    x.execute(Qur)
    # Create table with specified schema

    # Calculate ranks for location and incidents based on frequency
    LC = Counter(line[2] for line in Info)
    LR = {adr: pos for pos, 
        adrs in enumerate(sorted(LC.items(), 
        key=lambda x: x[1], reverse=True), start=1) 
        for adr in adrs}

    IC = Counter(line[3] for line in Info)
    IR = {inc: pos for pos, 
                    incs in enumerate(sorted(IC.items(),
                     key=lambda x: x[1], reverse=True), start=1) 
                     for inc in incs}

    for a, line in enumerate(Info, start=1):
        EMS = 0
        # Initialize EMS status
 
        if line[4] == "EMSSTAT":
            EMS = 1
            # Set EMS status to 1 if 'EMSSTAT' present in the row

        for b in range(1, 3):
        # Check next two rows for 'EMSSTAT' and set EMS status accordingly
            if a + b < len(Info):
                newLine = Info[a + b]
                if (line[0] == newLine[0] and line[2] == newLine[2] and newLine[4] == "EMSSTAT"):
                    EMS = 1
                    break
        
        if (line[0] == 'D'):
            print(line)
            # Print row if it starts with 'D'
        
        DT = line[0]
        LRank = LR[line[2]]
        Nature = line[3]
        IRank = IR[line[3]]
        addr = line[2]
        
        # Extract relevant data from the row
        IncTime = datetime.strptime(line[0], "%m/%d/%Y %H:%M")
        Day = (IncTime.isoweekday() % 7) + 1
        DHour = IncTime.hour 
        
        Wea  = Weather(addr, DT)
        # call weather function
        ToSide = TownSide(addr)
        # call location function
        
        # Extend row with additional data
        line.extend([Day, DHour, Wea, LRank, IRank, Nature, ToSide, EMS])

        NQur = f"INSERT INTO {Tab} VALUES ({', '.join(['?' for _ in line])})"
        x.execute(NQur, line)
        

    y.commit()
    # Commit changes
    y.close()
        # Close database connection

# def PopulateDB(Norman, Tab, Line):
# # Function to populate the SQLite database with incident parsed data
    
#     con = sqlite3.connect(Norman) # Connect to SQLite database
#     cur = con.cursor() # Create a cursor object for database operation

#     #Insert data in table
#     AddQ = "INSERT INTO {} VALUES ({});".format(Tab, ', '.join(['?']*len(Line[0])))

#     # Iterate through each row of data and insert it into the table
#     for DL in Line:
#         if len(DL) < 5 :
#             tmp = [''] * 5
#             cur.execute(AddQ, tmp)
#         else :
#             cur.execute(AddQ, DL)

#     cur.connection.commit() # Commit changes to the database

#     con.commit()
#     con.close() # Close the database connection


def Coord(address):
    # Function to get latitude and longitude of an address
    Mykey = "f763c93a2cb64f6bb651a0a7d741e58b"
    # My API key for Geoapify
    link = f"https://api.geoapify.com/v1/geocode/search?text={address}&limit=1&apiKey={Mykey}"
    
    r = requests.get(link)
    # Make request to Geoapify API

    if r.status_code == 200:  
        # If request successful
        resp = r.json()  
        # Get JSON data from response

        if (len(resp["features"]) == 0):
            Lat = None
            Long = None
        else :    
            result = resp["features"][0]
            Lat = result["geometry"]["coordinates"][1]
            # Extracting latitude
            Long = result["geometry"]["coordinates"][0]
            # Extracting longitude
        return Lat, Long
        # Return latitude and longitude
    else:
        print(f"Error Code: {r.status_code}")
        # Print error message
        return None, None

    
def TownSide(loc, CenLat=35.220833, CenLong=-97.443611):
    # Function to determine the side of town based on location coordinates
    LocLat, LocLon = Coord(loc)
    # Get latitude and longitude of location by calling location function

    if (LocLat == None or LocLon == None):
        return "Error"
    # Return error message if latitude or longitude cannot be extracted

    IncLat = float(LocLat) - CenLat
    IncLon = float(LocLon) - CenLong

    TurnAng = math.degrees(math.atan2(IncLon, IncLat))
    # Calculate angle
    
    Direct = ['E', 'SE', 'S', 'SW', 'W', 'NW', 'N', 'NE', 'E']  
    # Defining compass directions
    CalcAng = round(TurnAng / 45) % 8  
    return Direct[CalcAng]  
    # Return direction based on index

def Weather(Addr, Dat):
    # Function to get weather code for a location and time
    lat, lon = Coord(Addr)  
    # Get latitude and longitude of location
    
    IncTime = datetime.strptime(Dat, "%m/%d/%Y %H:%M")  
    # Parse incident time
    
    SDate = IncTime.date()  
    # Get start date
    EDate = IncTime.date()  
    # Get end date
    HourTime = IncTime.hour  
    # Get hour of the incident
    
    Cache = requests_cache.CachedSession('.cache', expire_after=-1)  
    # Create cached session
    RetryCache = retry(Cache, retries=5, backoff_factor=0.2)  
    # Create retry session
    OP = openmeteo_requests.Client(session=RetryCache)  
    # Create OpenMeteo client

    url = "https://archive-api.open-meteo.com/v1/archive"  
    # Define URL
    Attr = {  
        "latitude": "26.27332703176929", "longitude": "-81.6216394463461", "start_date": SDate, "end_date": EDate, "hourly": ["temperature_2m", "precipitation", "weather_code"]}
    # Define parameters
    r = OP.weather_api(url, params=Attr)  
    # Make request to OpenMeteo API
    x = r[0] 

    IncHour = x.Hourly()  
    # Get hourly data
    IncHourTemp = IncHour.Variables(0).ValuesAsNumpy()  
    # Get temperature data
    IncHourPre = IncHour.Variables(1).ValuesAsNumpy()  
    # Get precipitation data
    IncHourWeat = IncHour.Variables(2).ValuesAsNumpy()  
    # Get weather code data

    # Create hourly data dictionary
    HourDat = {"date": pd.date_range(  
        start=pd.to_datetime(IncHour.Time(), unit="s", utc=True), end=pd.to_datetime(IncHour.TimeEnd(), unit="s", utc=True),
        freq=pd.Timedelta(seconds=IncHour.Interval()), inclusive="left")}

    HourDat["temperature_2m"] = IncHourTemp  
    # Add temperature data
    HourDat["precipitation"] = IncHourTemp  
    # Add precipitation data
    HourDat["weather_code"] = IncHourWeat  
    # Add weather code data

    HourDF = pd.DataFrame(data=HourDat)  
    # Create DataFrame from hourly data
    return int(HourDF.iloc[HourTime]['weather_code'])  
    # Return weather code for the specified time


def Output(Norman, Tab):
    # Function to print contents of table in the database
    y = sqlite3.connect(Norman)  
    # Connect to SQLite database
    x = y.cursor()  
    # Create a cursor object

    x.execute(f"SELECT Day_of_the_Week, Time_of_Day, Weather, Location_Rank, Side_of_Town, Incident_Rank, Nat, EMSSTAT FROM {Tab}")  
    # Execute SQL query

    lines = x.fetchall()  

    df = pd.DataFrame(columns=["Day of week", "Time of Day", "Weather", "Location Rank", "Side of Town", "Incident Rank", "Nature", "EMSSTAT"])
    for line in lines:
        df.loc[len(df)] = line  
        # Append row to DataFrame
        
    print(df.to_markdown())
    y.close()  
    # Close database connection

def Insert(Information, Latest):
    # Function to insert and process information
    # Initialize a list to store latest table entry
        # Latest = []
        #print(Latest)
        for Row in Information:
        # Append rows with length greater than 1 to the Latest list
            if len(Row) > 1:
                Latest.append(Row)

    # Return the latest information
        return Latest

def main(urls_file):
    # Main function to process URLs and retrieve incident data
    with open(urls_file, 'r') as file:
        # Open URLs file
        urls = file.readlines()
        #print("Found URLs:", urls)
        # Read URLs
        Latest =[]
        for url in urls:
            url = url.strip()
            #print("Processing URL:", url)
            # Remove leading/trailing whitespaces
            incident_data = RetrieveIncidents(url) 
            # Call function to Retrieve incidents
            incidents = ExractData(incident_data)
            # Call function to Extract incidents
            Next = incidents.strip().split('\n')
            # Split incidents into lines
            Header = re.split(r'\s{2,}', Next[2].strip())
            Information = [re.split(r'\s{2,}', line.strip()) for line in Next[3:-1]]
            Latest = Insert(Information, Latest)

    
    Norman = "resources/normanpd.db" # Database name
    Tab = "incident_table" # Table name
    # print(Latest)
    DataBase(Norman, Tab, Latest)
    # Call Database function
    Output(Norman, Tab)
    # Print contents of the table

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--urls", type=str, required=True, help="File containing URLs of incidents.")
    args = parser.parse_args()
    if args.urls:
        main(args.urls)
        # Call main function with URLs file
