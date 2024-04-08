# **Datasheet**

## Dataset Description
This dataset contains augmented data from various incident PDF files provided by the Norman, Oklahoma police department's [webiste](https://www.normanok.gov/public-safety/police-department/crime-prevention-data/department-activity-reports). The purpose of this dataset is to provide additional context and information to support further processing in a data pipeline.

## Data Fields
| Field | Data Type | Description |
| --- | --- | --- |
| Day of the Week | Integer | The day of the week, where 1 corresponds to Sunday and 7 corresponds to Saturday. |
| Time of Day | Integer | The hour of the incident, ranging from 0 to 23. |
| Weather | Integer | The WMO (World Meteorological Organization) weather code, representing the weather conditions. |
| Location Rank | Integer | The rank of the location based on frequency, with ties preserved. |
| Side of Town | String | The side of town where the incident occurred, one of {N, S, E, W, NW, NE, SW, SE}. |
| Incident Rank | Integer | The rank of the incident type based on frequency, with ties preserved. |
| Nature | String | The direct text of the incident type from the source record. |
| EMSSTAT | Boolean | Indicates whether the incident was related to EMSSTAT. |

## Data Collection and Preprocessing
The data for this dataset was extracted from various PDF files provided by the Norman, Oklahoma police department's [webiste](https://www.normanok.gov/public-safety/police-department/crime-prevention-data/department-activity-reports). The URLs for these PDF files were provided in a separate file, which was used as input to the data processing script. The script read the PDF files, extracted the relevant information, and performed data augmentation to generate the additional fields.

## Data Augmentation
The data augmentation process involved generating the following additional fields:

- **Day of the Week**: Determined by parsing the date information from the source records and converting it to a day of the week value (1-7).
- **Time of Day**: Determined by parsing the time information from the source records and converting it to the hour of the day (0-24).
- **Weather**: Determined by analyzing the weather description in the source records and mapping it to the corresponding WMO weather code.
- **Location Rank**: Determined by ranking the locations based on their frequency, preserving ties.
- **Side of Town**: Determined by calculating the approximate direction of the location relative to the center of town coordinates.
- **Incident Rank**: Determined by ranking the incident types based on their frequency, preserving ties.
- **EMSSTAT**: Determined by checking if the Incident ORI was EMSSTAT or if the subsequent record or two contained an EMSSTAT at the same time and location.

## Dataset Limitations and Biases
The dataset may have geographic or demographic biases, as the source PDF files may not be representative of the entire population. Additionally, the data quality and completeness may be limited by the quality and consistency of the source records.

## Intended Use and Potential Misuse
This dataset is intended to be used as part of a larger data pipeline, providing additional context and information to support further processing and analysis. Potential misuses could include using the dataset for purposes outside of its intended scope, or making decisions based on incomplete or biased data.

## Maintenance and Updates
The dataset will be maintained and updated as new PDF files become available. The data processing script will be updated to handle any changes in the source data format or structure.

## Ethical Considerations
The dataset does not contain any personally identifiable information, but there may be privacy concerns related to the nature of the incident data. Care should be taken to ensure the dataset is used in an ethical and responsible manner, respecting individual privacy and avoiding potential harm or discrimination.

# DATASET OVERVIEW

## Basics: Contact, Distribution, Access


**1. Dataset name:** -> Oklahoma Norman police department's Incident Dataset.

**2. Dataset version number or date:**  -> Version 1.0 (4th April 2024)

**3. Dataset owner/manager contact information, including name and email:** -> Aryaan Shaikh  <<am.shaikh@ufl.edu>>

**4. Who can access this dataset (e.g., team only, internal to the company, external to the company):?**  -> This dataset is in a private repository and can only be accessed by [Dr. Christan Grant](https://github.com/cegme) and our Teaching Assistant [Yifan Wang](https://github.com/wyfunique). 

**5. How can the dataset be accessed?** -> This dataset can be accessed by this [Assignment-2 Link](https://github.com/Aryaan03/cis6930sp24-assignment2) 


## Dataset Contents

**6. What are the contents of this dataset? Please include enough detail that someone unfamiliar with the dataset who might want to use it can understand what is in the dataset. Specifically, be sure to include:- What does each item/data point represent (e.g., a document, a photo, a person, a country)? - How many items are in the dataset? - What data is available about each item (e.g., if the item is a person, available data might include age, gender, device usage, etc.)? Is it raw data (e.g., unprocessed text or images) or features (variables)? - For static datasets: What timeframe does the dataset cover (e.g., tweets from January 2010–December 2020)?**

-> The dataset comprises augmented incident data sourced from PDF files provided by the Norman, Oklahoma police department's [webiste](https://www.normanok.gov/public-safety/police-department/crime-prevention-data/department-activity-reports). Each entry encapsulates a singular incident documented by the police department, ranging from criminal activities to accidents or other events necessitating police intervention. These entries offer a detailed glimpse into the occurrences within Norman, Oklahoma, serving as a valuable resource for subsequent analysis and decision-making processes.

Each incident entry in the dataset is accompanied by a variety of data fields, furnishing comprehensive information about the incident's nature and contextual details. These fields include the day of the week, time of day, weather conditions, location rank, side of town, incident type rank, incident description, and an EMSSTAT indicator. Through data augmentation techniques, additional variables are generated to enhance the dataset, such as inferred day of the week, hour of the incident, and rankings based on frequency, facilitating deeper insights into the incidents recorded by the Norman, Oklahoma police department and aiding in comprehensive analysis of law enforcement trends and patterns in the region.

## Intended & Inappropriate uses

**7. What are the intended purposes for this dataset?**

-> The purpose of this dataset is to practice and learn data augmentation as part of CIS6930-Data Engineering Assignment project 2.

**8. What are some tasks/purposes that this dataset is not appropriate for?**

-> This dataset might not be suitable for tasks requiring individual identification or predictive modeling of individual behavior due to the lack of personally identifiable information. The aggregated nature of dataset also limits its applicability for generalizing findings to other geographic locations, as factors influencing incidents can vary significantly between regions. 

Moreover, while providing insights into local law enforcement trends, caution is needed when attempting broad generalization. Tasks requiring detailed legal or regulatory information may also be unsuitable, given the dataset's focus on incident data. Additionally, while including weather information, it may not be comprehensive for historical weather analysis. Overall, while valuable for specific law enforcement and public safety analyses, its limitations restrict its applicability for tasks requiring individual-level data, predictive modeling, or broad generalization to diverse contexts.


## Data Collection Procedures

**9. How was the data collected? Describe data collection procedures and instruments. Describe who collected the data (e.g., contractors).**

-> The data was collected by extracting information from PDF files on the Norman, Oklahoma police department's [webiste](https://www.normanok.gov/public-safety/police-department/crime-prevention-data/department-activity-reports). Data extraction using pypdf was used in parsing text to identify incident details. Furthermore, augmentation processes were used to enrich the dataset by genrating additional fields. The collection of data may have been conducted by internal staff or contracted data analysts of Oklahoma's Norman police department.

**10. Describe considerations taken for responsible and ethical data collection (e.g., procedures, use of crowd workers, recruitment, compensation).**

-> While the dataset doesn't include any personally identifiable information, privacy concerns may arise due to the sensitive nature of the incident data. It's crucial to handle the dataset ethically and responsibly, prioritizing individual privacy and preventing potential harm or discrimination. Thus, careful consideration must be given to ensure respectful and ethical usage of the dataset.

**11. Describe procedures and include language used for getting explicit consent for data collection and use, and/or revoking consent (e.g., for future uses or for certain uses). If explicit consent was not secured, describe procedures and include language used for notifying people about data collection and use.**

-> Does not apply as the source of extracting data is incident records from Oklahoma's Norman police department.

## Representativeness

**12. How representative is this dataset? What population(s), contexts (e.g., scripted vs conversational speech), conditions (e.g., lighting for images) is it representative of? How was representativeness ensured or validated? What are known limits to this dataset’s representativeness?**

-> This dataset represents incident data from Oklahoma, potentially reflecting law enforcement trends in Oklahoma city. Representativeness may be validated through comparisons with official crime statistics of different cities incident reports. However, limitations may include potential biases in reporting and variations in law enforcement practices across jurisdictions.

**13. What demographic groups (e.g., gender, race, age, etc.) are identified in the dataset, if any? How were these demographic groups identified (e.g., self-identified, inferred)? What is the breakdown of the dataset across demographic groups? Consider also reporting intersectional groups (e.g., race x gender) and including proportions, counts, means or other relevant summary statistics.**

-> The dataset does not explicitly identify demographic groups such as gender, race, or age. There is limited information on the representation of demographic groups or intersectional analyses within the dataset.

## Data Quality
**14. Is there any missing information in the dataset? If yes, please explain what information is missing and why (e.g., some people did not report their gender).**

-> The dataset description doesn't explicitly mention missing information, but potential gaps could exist in incident reports. Missing data might include incomplete incident descriptions or omitted details such as specific location coordinates. Reasons for missing information could vary, including incomplete reporting by law enforcement or redaction of sensitive details for privacy reasons.

**15. What errors, sources of noise, or redundancies are important for dataset users to be aware of?**

-> Errors may arise from manual data entry or transcription inaccuracies, sources of noise could include duplicate entries, impacting dataset's integrity and redundancies may occur due to multiple records of the same incident or overlapping information.

**16. What data might be out of date or no longer available (e.g., broken links in old tweets)?**

-> Incident reports may become out of date or unavailable over time. For example, links to PDF files containing incident data might be removed from the website, rendering the associated data inaccessible.

**17. How was the data validated/verified?**

-> There is no way to validate or verify the data.

**18. What are potential validity issues a user of this dataset needs to be aware of (e.g., survey answers might not be truthful, age was guessed by a model and might be incorrect, GPA was used to quantify intelligence)?**

-> Incident details may vary in accuracy, and inferred variables like nature or location may introduce uncertainties.

**19. What are other potential data quality issues a user of this dataset needs to be aware of?**

-> Users should be cautious of inconsistencies, missing data, biases, and errors inherent in incident records. Redundancies, outdated information, and limited context may also impact data quality.

## Pre-Processing, Cleaning, and Labeling

**20. What pre-processing, cleaning, and/or labeling was done on this dataset? Include information such as: how labels were obtained, treatment of missing values, grouping data into categories (e.g., was gender treated as a binary variable?), dropping data points.Who did the pre-processing, cleaning, and/or labeling (e.g., were crowd workers involved in labeling?)**

-> The dataset underwent several pre-processing and cleaning steps to ensure data quality. Incident details were extracted from PDF files and augmented to derive additional fields such as day of the week, time of day, and weather conditions. Labels for incident types were obtained from the source records. 

Missing values were handled through imputation or dropped. Categorical variables like incident type and location were grouped and ranked based on frequency. Pre-processing and cleaning were performed by Aryaan Shaikh.

**21. Provide a link to the code used to preprocess/clean/label the data, if available.**

-> The link to code is: https://github.com/Aryaan03/cis6930sp24-assignment2/blob/main/assignment2.py


**22. If there are any recommended data splits (e.g., training, development/validation, testing), please explain.**

-> There are no recommended data splits.

## Privacy

**23. What are potential data confidentiality issues a user of this dataset needs to be aware of? How might a dataset user protect data confidentiality?**

-> Potential data confidentiality issues include the risk of exposing sensitive incident details. Users should handle the data responsibly, ensuring it's accessed and used only for lawful and ethical purposes. To protect data confidentiality, users can implement access controls and encryption.

**24. Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset? Does the dataset contain data that might be considered sensitive in any way (e.g., data that reveals race, sexual orientation, age, ethnicity, disability status, political orientation, religious beliefs, union memberships; location; financial or health data; biometric or genetic data; criminal history) If the answer to either of these questions is yes, please be sure to consult with a privacy  expert and receive approvals for storing, using, or distributing this dataset.**

-> The dataset does not contain any personally identifiable information. However, it may contain incident data that could indirectly identify individuals when combined with external information. Additionally, sensitive information such as location, incident details, and potentially demographic factors may be present, raising privacy concerns.

**25. If an analysis of the potential impact of the dataset and its uses on data subjects (e.g., a data protection impact analysis) exists, please provide a brief description of the analysis and its outcomes here and include a link to any supporting documentation.**

-> Doesn't apply for this dataset. No such analysis of potential impact of the dataset and its uses on data subjects exists.

**26. If the dataset has undergone any other privacy reviews or other relevant reviews (legal, security) please include the determinations of these reviews, including any limits on dataset sage or distribution.**

-> The dataset has not undergone any other privacy reviews or other relevant reviews.

## Additional Details on Distribution & Access

**27. How can dataset users receive information if this dataset is updated (e.g., corrections, additions, removals)?**

-> Dataset users can receive information about updates, corrections, additions, or removals through GItHub through version updates.

**28. For static datasets: What will happen to older versions of the dataset? Will they continue to be maintained?**

-> For static datasets, older versions may removed as Oklahoma Norman PD can remove incident records making earlier url's invalid. 

**29. For streaming datasets: If this dataset pulls telemetry data from other sources, please specify:- What sources; - How frequently the dataset is refreshed.Who controls access to these sources- Whether access to these sources will remain available, and for how long; - Any applicable access restrictions to these sources including licenses and fees; - Any other available access points to these sources; - Any relevant information about versioning. Are there any other ways in which these sources might affect this dataset that a dataset user needs to be aware of?**

-> <u>Sources</u> - [Norman, Oklahoma police department's webiste](https://www.normanok.gov/public-safety/police-department/crime-prevention-data/department-activity-reports)

-> <u>Access Control</u> - Incident records access is controlled by Norman, Oklahoma police department.
The dataset control access is with Aryaan Shaikh.

**30. If this dataset links to data from other sources (e.g., this dataset includes links to content such as social media posts or, news articles, but not the actual content), please specify: - What sources;- Whether access to these sources will remain available, and for how long; - Who controls access to these sources;- Any applicable access restrictions to these sources including licenses and fees;- For static datasets: If an official archival version of the complete dataset exists (i.e., including the content as it was at the time the dataset was created), where it can be accessed. Are there any other ways in which these sources might affect this dataset that a dataset user needs to be aware of?**

-> The data is not linked to any other source.

**31. Describe any applicable intellectual property (IP) licenses, copyright, fees, terms of use, export controls, or other regulatory restrictions that apply to this dataset or individual data points. These might include access restrictions related to data subjects’ consenting or being notified of data collection and use, as well as revoking consent. Provide links to or copies of any such applicable terms.**

-> There are no applicable intellectual property (IP) licenses, copyright, fees, terms of use, export controls, or other regulatory restrictions.

# Contact Information
For questions or feedback about this dataset, please contact the dataset maintainers at [am.shaikh@ufl.edu].