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

**Datasheets link**:- 

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

video link: [Data Engineering Assignment2 demo](https://github.com/Aryaan03/cis6930sp24-assignment1/blob/main/DE_Assignment-1_Demo.mp4)
<br>
![](https://github.com/Aryaan03/cis6930sp24-assignment1/blob/main/DE_Assignment-1_DemoGIF.gif)<br>
The video is also available in the repository in good quality.<br>

## Functions
#### main 

   1. `Argparse()`<br>
         • Description:<br>
         &emsp;&emsp;- This function sets up an argument parser using the `argparse` module to parse command-line arguments.<br>
         &emsp;&emsp;- It defines various command-line arguments such as input files, output directory, censoring flags (names, dates, phones, address), and statistics.<br>
         • Parameters:<br>
      &emsp;&emsp;- None<br>
         • Return:<br>
         &emsp;&emsp;- Parsed arguments object (`argparse.Namespace`) object containing the parsed arguments.<br>

  2. `CenName(MailData)`<br>
        • Description:<br>
          &emsp;&emsp;- This function utilizes the spaCy model to extract names (entities labeled as "PERSON") from the input text.<br>
          &emsp;&emsp;- Extracts person names from the provided text data.<br>
         • Parameters:<br> 
       &emsp;&emsp;- `MailData` - Input text data. <br>
         • Returns: <br>
       &emsp;&emsp;- A list containing the extracted person names from the provided text data..<br>

  3. `CenDate(MailData)`<br>
         • Description: <br>
           &emsp;&emsp;- This function uses the Google Cloud Natural Language API to analyze entities in the text and extracts dates.<br>
           &emsp;&emsp;- Extracts dates from the provided text data.<br>
         • Parameters:<br>
         &emsp;&emsp;- `MailData` - Input text data.<br>
        • Returns: <br>
        &emsp;&emsp;- A list containing the extracted dates from the provided text data.<br>
    
  5. `CenNum(MailData)`<br>
         • Description: <br>
           &emsp;&emsp;- Similar to CenDate(), this function uses the Google Cloud Natural Language API to analyze entities and extracts phone numbers. <br>
           &emsp;&emsp;- Extracts phone numbers from the provided text data.<br>
         • Parameters:<br>
         &emsp;&emsp;- `MailData` - Input text data.<br>
         • Returns: <br>
          &emsp;&emsp;- A list containing the extracted phone numbers from the provided text data.<br>
    
  5. `CenLoc(MailData)`<br>
         • Description: <br>
                 &emsp;&emsp;- Similar to the CenDate() and CenNum() functions, it uses the Google Cloud Natural Language API to extract addresses from the input text.<br>
                 &emsp;&emsp;- Extracts addresses from the provided text data.<br>
            • Parameters: <br>
            &emsp;&emsp;- `MailData` - Input text data.<br>
            • Returns: <br>
            &emsp;&emsp;- A list containing the extracted addresses from the provided text data.<br>

   6. `analyze_entities(MailData, FlaTyp)`<br>
        • Description: <br>
         &emsp;&emsp;- This function coordinates the analysis of entities based on the flags provided..<br>
         &emsp;&emsp;- It calls other functions based on the flags set in FlaTyp and collects statistics.<br>
        • Parameters:<br>
           &emsp;&emsp;- `MailData`: The input text to be analyzed.<br>
           &emsp;&emsp;- `FlaTyp`: Dictionary containing flags indicating which types of entities to analyze.<br>
        • Return: <br>
        &emsp;&emsp;- A tuple containing a list of entities found in the text and a list of statistics regarding the entities (statistics of dates, phone numbers, addresses, and person names).<br>
    
  7. `censor(info, type)`<br>
   • Description: <br>
        &emsp;&emsp;- This function replaces sensitive information in a given string with a block character.<br>
        &emsp;&emsp;- Uses unicode character '█' (U+2588) to censor sensitive data.<br>
        • Parameters:<br>
            &emsp;&emsp;`info`: The input string containing sensitive text.<br>
            &emsp;&emsp;`type`: A list of strings representing sensitive text.<br>
        • Return:<br>
         &emsp;&emsp;- The input string with sensitive information replaced by block characters.<br>

   8. `CenP(data, FlaTyp)`<br>
        • Description: <br>
        &emsp;&emsp;- This function censors sensitive information based on the flags provided.<br>
        &emsp;&emsp;- calls `analyze_entities` and `censor` function to replace identified entities with block characters to obscure sensitive details.<br>
        &emsp;&emsp;- It also prints or writes statistics about the censored information.<br>
        • Parameters:<br>
            &emsp;&emsp;- `data`: The text data to be censored.<br>
            &emsp;&emsp;- `FlaTyp`: Dictionary containing flags indicating which types of entities to analyze.<br>
        • Return: <br>
        &emsp;&emsp;- The censored text data.<br>

   9.    `case(x)`<br>
        • Description: <br>
        &emsp;&emsp;- This function filters out tokens using Regex.<br>
        &emsp;&emsp;- Prepares a list of tokens excluding digit-only entries for subsequent processing.
        • Parameters:<br>
            &emsp;&emsp;- `x`: A list of strings (tokens).<br>
        • Return: <br>
        &emsp;&emsp;- Filtered list of elements.<br>

   10. `Read(Xtemp, CCd, FlaTyp)`<br>
        • Description: <br>
        &emsp;&emsp;- This function reads input files, calls `CenP()` function to censore sensitive information in the text.<br>
        &emsp;&emsp;- Writing censored text to a new file.<br>
        &emsp;&emsp;- Ensures secure handling of sensitive text during file processing.<br>
        • Parameters:<br>
            &emsp;&emsp;- `Xtemp`: A list of file paths to be read.<br>
            &emsp;&emsp;- `CCd`: The directory where censored files will be saved.<br>
            &emsp;&emsp;- `FlaTyp`: Dictionary containing censoring flags.<br>
        • Return: <br>
        &emsp;&emsp;- None.<br>

   11. `main()`<br>
        • Description: <br>
        &emsp;&emsp;- This function serves as the main entry point of the script.<br>
        &emsp;&emsp;- It parses command-line arguments, identifies input files, processes them, and performs censorship based on specified flags.<br>
        &emsp;&emsp;- Creates an output directory if it doesn't exist.<br>
        &emsp;&emsp;- Handles some exceptions like Printing an error message to prompt user for specifing censoring flags.<br>
        &emsp;&emsp;- Prints error message if input files is not found.<br>
        • Parameters: <br>
        &emsp;&emsp;- None<br>
        • Return: <br>
        &emsp;&emsp;- None.<br>
        
        
## Testing

Testing using pytest & mocking is done to make sure that all the functions are working independently and properly. Testing is crucial for early bug detection and maintaining code quality. Testing units of code encourages modular, understandable code and integrates seamlessly into continuous integration workflows, boosting integrity. The given unittesting code tests various functions related to censoring sensitive information such as names, dates, addresses, and phone numbers in a given text. Ultimately, all major functions like test_names, test_dates, test_addresses, test_phone_numbers and more are tested if they are functioning properly. For example. test_names verifies if the spacy model is able to identify names in the given text file. 

    1.  `test_censor_function`
        Purpose: 
        - Tests the `censor` function, which is expected to replace sensitive information in a given text with a block character.
        Steps:
            -> Defines test data including the input text (tempdata), detected entities (Detected), and the expected output after censoring (out).
            -> Invokes the `censor` function with the test data.
            -> Asserts that the output matches the expected output

     2. `test_names` 
        Purpose: 
        -  Tests the `CenName` function, which is expected to detect names in a given text.
        Steps:
             -> Mocks the Spacy model using the @patch decorator.
             -> Defines mock data for the Spacy model to return.
             -> Sets up test data containing input text (tempdata) and the expected detected names (out).
             -> Invoke the `CenName` function with the test data.
             -> Assert that the detected names match the expected output.

    3. `test_dates`
        Purpose: 
        - Tests the `CenDate` function, which is expected to detect dates in a given text.
        Steps:
             -> Mock the Google Cloud NLP API using the @patch decorator.
             -> Define mock data for the API response.
             -> Set up test data containing input text (tempdata) and the expected detected dates (out).
             -> Invoke the `CenDate` function with the test data.
             -> Assert that the detected dates match the expected output.

    4. `test_addresses`
        Purpose: 
        - Tests the `CenLoc` function, which is expected to detect addresses in a given text.
        Steps:
             -> Mock the Google Cloud NLP API using the @patch decorator.
             -> Define mock data for the API response.
             -> Set up test data containing input text (tempdata) and the expected detected addresses (out).
             -> Invoke the `CenLoc` function with the test data.
             -> Assert that the detected addresses match the expected output.

    5. `test_phone_numbers`
        Purpose: 
        - Tests the `CenNum` function, which is expected to detect phone numbers in a given text.
        Steps:
              -> Mock the Google Cloud NLP API using the @patch decorator.
              -> Define mock data for the API response.
              -> Set up test data containing input text (tempdata) and the expected detected phone numbers (out).
              -> Invoke the `CenNum` function with the test data.
              -> Assert that the detected phone numbers match the expected output.

## Bugs and Assumptions

• Assuming that atleast any one of the flag should be given in the run command. <br>
• A large text files or a high volume of data exceeding system memory or processing limits, can lead to performance degradation or application crashes.<br>
• All the entities are not accurately detected, it leaves some entities according to the model selected.<br>
• I have used en_core_web_md model as given in assignment description. I could have used the large model(en_core_web_md) but it detects some extra data which should not be sensored compared to the Spacy medium English model.<br>
• Known bug: Some txt files with unsual formatting are not able to parse.<br> 
• It does not check censor names in email addresses. <br>
• No bugs apart from those mentioned above are known/identified.


## Version History

• 0.1 <br>
   &emsp;&emsp; -> Initial Release

## License

This project is licensed by Aryaan Shaikh©2024.

## Acknowledgments

• [Christan Grant](https://github.com/cegme)- Providing the problem Statement <br>
• [Yifan Wang](https://github.com/wyfunique)- Testing our code<br>
• [Pipenv: Python Dev Workflow for Humans](https://pipenv.pypa.io/en/latest/)- Helped me in Installing Pipenv <br>
• [Google API services](https://cloud.google.com/products?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-b-dr-1707554&utm_content=text-ad-none-any-DEV_c-CRE_665735422238-ADGP_Hybrid+%7C+BKWS+-+MIX+%7C+Txt-Google+Products-Google+Products+General-KWID_43700077225654153-kwd-305853018146&utm_term=KW_google%20cloud%20api-ST_google+cloud+api&gad_source=1&gclid=CjwKCAiA0bWvBhBjEiwAtEsoW4c9xSrIqN7aa-RqxnDZEvpJvMpjHFvof4xKSOGmutlJ6hapBB_iPBoCW4kQAvD_BwE&gclsrc=aw.ds)- Helped me in understanding google maps API usage<br>
• [Cloud Natural Language API](https://cloud.google.com/natural-language/docs/reference/rest)- Documentation reference for understanding GCP Cloud Natural Language API<br> 
• [Spacy Models](https://spacy.io/models/en)- Documentation for English Spacy Models <br>
• [NLTK Tokenize](https://www.nltk.org/api/nltk.tokenize.html)- Documentation for nltk.tokenize package <br>
