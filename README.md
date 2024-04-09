# CIS6930sp24 -- Assignment2

Name: Aryaan Shaikh <br>
Student ID: 3020-2476

## Contact

Email - am.shaikh@ufl.edu <br>
Project Link: https://github.com/Aryaan03/cis6930sp24-assignment2


## Assignment Description
This is the 3rd project assignment for the CIS6930 Data Engineering course and is an extension to a previous [Assignment0](https://github.com/Aryaan03/cis6930sp24-assignment0). The main aim of this assignment is to practice data augmentation. In this assignment, we will input url links from a .csv file and for each URL, we'll be extracting incident data from PDF files provided by the Norman, Oklahoma police department's webiste [link](https://www.normanok.gov/public-safety/police-department/crime-prevention-data/department-activity-reports). We'll then use data augmentation techniques to generate additional features for each record. This will involve tasks like assigning a day-of-week value, determining the time of day for the incident, and even fetching the weather data for the location. We'll also be ranking the frequency of locations and incident types to add context to the data. Finally, we'll analyze the data to determine if an EMS response was likely. <br> 

The ultimate goal here is to create a more informative dataset that can be used for further analysis. To ensure everyone understands this new dataset, we'll put together a detailed data sheet. This will document the entire process we followed, explain each feature in the dataset, and highlight any potential data quality issues we encounter. By the end of this project, we'll have a comprehensive dataset along with a data sheet that guides its use.<br>

To Conclude, this is a great assignment that emphasizes augmenting data extraction and gaining more relevant information from data. , sensitivity in handling private information, and efficiency in data processing. It helped us to learn more about data pipeline processes and also presents a hands-on opportunity to engage with real-world data scenarios, nurturing skills vital in the domain of data engineering.
<br>


### Datasheets

Datasheets are like instruction manuals for datasets. They provide a clear and concise explanation of what data points are included, what they represent, and how they're formatted. This is especially beneficial for our enriched incident report dataset.  Having a datasheet ensures everyone using the data understands its content and interprets it consistently. Furthermore, datasheets promote collaboration and future analysis.  They document the entire process of creating the data, allowing others to replicate it or understand potential limitations. For instance, the datasheet might mention inconsistencies in how locations were reported. This transparency empowers future data users to make informed decisions and avoid misinterpretations. With a datasheet, your enriched dataset becomes a valuable shared resource.<br><br>

**Datasheets link**:- <u>https://github.com/Aryaan03/cis6930sp24-assignment2/blob/main/datasheet.md</u>

## How to install
```
pipenv install 
```

## How to run
Project can be run by using any of the given commands:
```
pipenv run python assignment2.py --urls files.csv
```

For testing use command:
```
pipenv run python -m pytest
```

## Demo Implementation 

video link: [Data Engineering Assignment3 demo](https://github.com/Aryaan03/cis6930sp24-assignment1/blob/main/DE_Assignment-1_Demo.mp4)
<br>
The video is also available in the repository in good quality.<br>

## Functions
#### main 
1. `RetrieveIncidents(url)`<br>
    • Description: <br>
        &emsp;- Downloads/Fetches incident data from a given URL.<br>
        &emsp;- The `urllib.request` module is used to execute an HTTP request and retrieve the data.<br>
        &emsp;- Data is stored locally in a local variable and not at any specific location (tmp folder) for using it for both making a SQL database and also for retreiving data.<br>
        &emsp;- Constructs a request with a custom user agent to access the provided URL.<br>
    • Parameters: <br>
        &emsp;- `url`(str), The URL from which the incident data is to be fetched.<br>
    • Returns:<br>
        &emsp;- `data`; The fetched incident data.<br>

2. `ExtractData(IncidentData)`<br>
    • Description: <br>
        &emsp;- This function extracts incident information from the incident PDF file using Pypdf.<br>
        &emsp;- Reads the incident data from a PDF using `pypdf.PdfReader` and `io.BytesIO`.<br>
        &emsp;- Extracts text from each page of the PDF using the layout mode and concatenates it into a single string.<br>
    • Parameters: <br>
        &emsp;- `IncidentData`(bytes), The incident data in PDF format.<br>
    • Returns:<br>
        &emsp;- `ExtractText`; The extracted text from the incident data PDF.<br>

3. `Database(Norman, Tab, Info)`<br>
    • Description: <br>
        &emsp;- This function creates and populates an SQLite database and a table based on the provided parameters using the `sqlite3` module.<br>
        &emsp;- Defines the table schema and creates the table if it doesn't exist. <br>
        &emsp;- Calculates ranks for location and incidents based on frequency.<br>
        &emsp;- Inserts data into the table with additional calculations.<br>
    • Parameters: <br>
        &emsp;- `Norman`(str); The name of the SQLite database file.<br>
        &emsp;- `Tab`(str); The name of the table to be created.<br>
        &emsp;- `Info`(list); List containing incident information in the form of tuples.<br>
    • Returns:<br>
        &emsp;- None<br>

4. `Coord(address)`<br>
    • Description: <br>
        &emsp;- Retrieves latitude and longitude coordinates of a given address using Geoapify API.<br>
        &emsp;- Constructs a request to Geoapify API with the address.<br>
        &emsp;- Parses the response JSON to extract latitude and longitude.<br>
    • Parameters: <br>
        &emsp;- `address`(str); Address for which latitude and longitude coordinates are to be retrieved.<br>
    • Returns:<br>
        &emsp;- `Lat, Long`; Tuple of latitude and longitude coordinates (float, float) if coordinates are found, otherwise (None, None). <br>

5. `TownSide(loc, CenLat=35.220833, CenLong=-97.443611)`<br>
    • Description: <br>
        &emsp;- Determines the side of town based on location coordinates.<br>
        &emsp;- Calculates the angle between the location and the center of the town.<br>
        &emsp;- Maps the angle to a compass direction.<br>
    • Parameters: <br>
        &emsp;- `loc`(str); Location for which the side of the town is to be determined.<br>
        &emsp;- `CenLat`(float); Latitude of the center point of the town (default is 35.220833).<br>
        &emsp;- `CenLong`(float); Longitude of the center point of the town (default is -97.443611).<br>
    • Returns:<br>
        &emsp;- `Direct[CalcAng]`(str); String indicating the side of town ('N', 'E', 'S', 'W', etc.) based on the location.<br>
        
6. `Weather(Addr, Dat)`:<br>
    • Description: <br>
       &emsp;- Retrieves weather code for a given location and time using OpenMeteo API.<br>
       &emsp;- Constructs a request to OpenMeteo API with location and time parameters.<br>
       &emsp;- Retrieves weather data from the API response. <br>
    • Parameters: <br>
       &emsp;- `Addr`(str); Address for which weather information is to be retrieved.<br>
       &emsp;- `Dat`(str); Date and time of the incident in "mm/dd/yyyy hh:mm" format.<br>
    • Returns:<br>
       &emsp;- `int(HourDF.iloc[HourTime]['weather_code'])`(int); Integer representing the weather code for the specified time and location.<br>

7. `Output(Norman, Tab)`:<br>
    • Description: <br>
       &emsp;- Prints the contents of a specified table in the SQLite database.<br>
       &emsp;- Executes a SQL query to select data from the specified table.<br>
       &emsp;- Fetches the data and prints it in a tabular format using Pandas.<br>
    • Parameters: <br>
       &emsp;- `Norman`(str); The name of the SQLite database file.<br>
       &emsp;- `Tab`(str); The name of the table to be created.<br>
    • Returns:<br>
       &emsp;- None; But it prints the contents of the specified table in the SQLite database.<br>
       
8. `Insert(Information, Latest)`<br>
    • Description: <br>
        &emsp;- Processes and inserts information into the database.<br>
        &emsp;- Filters out rows with length greater than 1 from the input.<br>
    • Parameters: <br>
        &emsp;- `Information` (list); List of incident information.<br>
        &emsp;- `Latest` (list); Previous information extracted from the incident data.<br>
    • Returns:<br>
        &emsp;- `Latest`(list); Latest information extracted from the incident data.<br>

9. `main(url)`:<br>
    • Description: <br>
        &emsp; - Invokes the process of retrieving incident data, processing it, and populating the database.<br>
        &emsp;- Reads URLs from a file.<br>
        &emsp;- Retrieves incident data from each URL.<br>
        &emsp;- Extracts and processes incident information. <br>
        &emsp;- Populates the database with the processed information.<br>
        &emsp;- Prints the contents of the database table.<br>
    • Parameters:<br>
        &emsp; - `urls_file`(str); File containing URLs of incidents.<br>
    • Returns:<br>
         &emsp; - None; But it orchestrates the whole process of retrieving incident data, processing it, and populating the database.

        
## Testing

Testing using pytest & mocking is done to make sure that all the functions are working independently and properly. Testing is crucial for early bug detection and maintaining code quality. Testing units of code encourages modular, understandable code and integrates seamlessly into continuous integration workflows, boosting integrity. Ultimately, all major functions like Retrieve, ExtractData, Database and more are tested if they are functioning properly. For example. test_retrieve verifies if data is fetched from the URL or not. 


    1. `test_Retrieve`:
        - Utilizes mocking to validate individual functions.
        - Uses mock versions of urllib.request.urlopen to simulate fetching data from a URL.
        - Dummy data ('Some Dummy data') is provided instead of actual network requests.
        - The URL variable serves as input for testing the fetchIncidents function.

    2. `test_Extraction`:
        - Mocks the PDF library to control page content.
        - Creates dummy pages with predefined text for testing text extraction.
        - Ensures the extracted text matches expected output, validating correct text extraction without real PDFs.

    3. `test_Create`:
        - Uses mocking to verify the createdb function successfully creates a database and table.
        - Checks if sqlite3.connect is called with correct arguments.
        - Verifies expected SQL queries are executed on the mock cursor.
        - Ensures commit and close methods are called on the mock connection.

    4. `test_Populate`:
        - Mocks sqlite3.connect to verify data insertion calls and expected queries.
        - Validates if commit and close occur on the mock connection.
        - Verifies data insertion follows table format, ensuring correct function behavior without a real database.

    5. `test_Status`:
        - Mocks the database connection to return desired data.
        - Captures printed output of the status function.
        - Compares captured output to expected string, verifying correct output generation using mocked data.

## Bugs and Assumptions

• Assuming that the structure of the PDF files provided by the Norman, Oklahoma police department remains consistent across different reports. If the structure changes, it could break the extraction process. <br>
• A large PDF files or a high volume of data exceeding system memory or processing limits, can lead to performance degradation or application crashes.<br>
• Not all columns of a row can be empty at the same time. There should be some entry in atleast one cell of every row.<br>
• All fields, excluding the 'Nature' field will consist of alphanumeric characters.<br>
• Assuming that empty entries are not only possible. If there are empty entries are encountered, it might break the extraction.<br>
• Known bug: Some pdfs that have unsual formatting are not able to parse.<br> 
• If there are multiple lines in a single cell, then only the first line will be parsed. There is no such cases where the 'Nature' column had multiple lines of text. So, it was not tested. But, if it has, this can be a potential bug.<br>
• The Runtime for this script is very high (around 10-15 mins for two url links), this is because I am using free API's and they each API call is taking a lot of time.
• No bugs apart from those mentioned above are known/identified.

## Version History

• 0.1 <br>
   &emsp;&emsp; -> Initial Release

## License

This project is licensed by Aryaan Shaikh©2024.

## Acknowledgments

• [Christan Grant](https://github.com/cegme)- Providing the problem Statement <br>
• [Yifan Wang](https://github.com/wyfunique)- Testing our code<br>
• [Geoapify Documentation](https://apidocs.geoapify.com/)- Helped me in understanding how to use Geoapify API key. <br>
• [Open-Meteo Documentation](https://open-meteo.com/en/docs)- Helped me in understanding the Weather API usage<br>
• [Pipenv: Python Dev Workflow for Humans](https://pipenv.pypa.io/en/latest/)- Helped me in Installing Pipenv <br>
• [Extract Text from a PDF](https://pypdf.readthedocs.io/en/latest/user/extract-text.html)- Helped me in extracting text in a fixed width format and changing cells<br>
 <br>
