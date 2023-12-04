import requests
import pandas as pd
import json

# List of study identifiers (NCT numbers)
# study_identifiers = ["NCT04550221", "NCT03875950", "NCT02735642"]  # Add more study identifiers as needed
study_identifiers = ["NCT04550221", "NCT03875950","NCT03574129", "NCT03054051","NCT03049917","NCT02915367","NCT02735642","NCT02400671","NCT04736316","NCT03928418","NCT03718871","NCT03435497","NCT03600142"] 


# Initialize an empty list to store the extracted data
all_extracted_data = []

# Loop through each study identifier and retrieve data
for identifier in study_identifiers:
    url = f"https://classic.clinicaltrials.gov/api/query/study_fields?expr={identifier}&fields=LeadSponsorName,InterventionDescription,BaselineMeasurePopulationDescription,DesignInterventionModelDescription,InterventionName,PrimaryOutcomeDescription&fmt=JSON"
    # url = f"https://classic.clinicaltrials.gov/api/query/full_studies?expr={identifier}&fmt=JSON"
    
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        
        extracted_data = {
            "NCTNumber": identifier,
            "LeadSponsorName": data["StudyFieldsResponse"]["StudyFields"][0]["LeadSponsorName"][0],
            "InterventionDescription": data["StudyFieldsResponse"]["StudyFields"][0]["InterventionDescription"][0] if data["StudyFieldsResponse"]["StudyFields"][0].get("InterventionDescription") else None,
            "BaselineMeasurePopulationDescription": data["StudyFieldsResponse"]["StudyFields"][0]["BaselineMeasurePopulationDescription"][0] if data["StudyFieldsResponse"]["StudyFields"][0].get("BaselineMeasurePopulationDescription") else None,
            "DesignInterventionModelDescription": data["StudyFieldsResponse"]["StudyFields"][0]["DesignInterventionModelDescription"][0] if data["StudyFieldsResponse"]["StudyFields"][0].get("DesignInterventionModelDescription") else None,
            "InterventionName": data["StudyFieldsResponse"]["StudyFields"][0]["InterventionName"][0],
            "PrimaryOutcomeDescription": data["StudyFieldsResponse"]["StudyFields"][0]["PrimaryOutcomeDescription"][0],
        }
        all_extracted_data.append(extracted_data)
    else:
        print(f"Failed to retrieve data for {identifier} with status code {response.status_code}")

# Once you have collected the data for all study identifiers, you can convert it into a Pandas DataFrame for further analysis or manipulation.
df = pd.DataFrame(all_extracted_data)
# # Save the data to a CSV file if needed
df.to_csv("clinical_trial_data.csv", index=False)

# # You can also perform various data analysis and manipulation tasks with the DataFrame
print(df.head())

# let us assess the Primary Outcomes Description of each trial
# Extract all Pri outcomes into one variable
pri_outcome = df['PrimaryOutcomeDescription']

# sentences = ' '.join(pri_outcome.astype(str))

sentences = pri_outcome
print(pri_outcome)



