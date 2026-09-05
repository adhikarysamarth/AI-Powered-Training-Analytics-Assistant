#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 16:20:05 2023

@author: samarth
"""

# Load Required Libraries
import pandas as pd
import numpy as np
import re
import datetime

# Load excel file into pandas dataframe
df = pd.read_excel("data/raw/Student_Data_Raw.xlsx", index_col=None)

# Inspect DataFrame
df.columns
df.dtypes
df.shape
df.isnull().sum()

# Simplify package names by eliminating unnecessary characters and words
df["Course Package"] = df["Course Package"].astype(str).apply(lambda x: x.split("_", 1)[1] if "_" in x else x)
df["Course Package"] = df["Course Package"].apply(lambda x: re.sub(r"_Package$", "", x,flags=re.IGNORECASE))
df["Course Package"] = df["Course Package"].apply(lambda x: x.split('_', 1)[1] if '_' in str(x) else x)
df["Lead Source"] = df["Lead Source"].apply(lambda x: x.split('_')[1] if '_' in str(x) else x)

# Rename the columns
df.rename(columns={"Enquiry Date": "Inquiry Date"}, inplace=True)
df.rename(columns={"Expected End Date": "End Date"}, inplace=True)
df.rename(columns={"Course Package": "Program"}, inplace=True)
df.rename(columns={"Counsellor": "Coordinator"}, inplace=True)

# Transform the date columns into the datetime data type
date_columns = ['Inquiry Date', 'Start Date', 'End Date', 'Admission Date']

for col in date_columns:
    df[col] = pd.to_datetime(df[col], format='mixed', errors='coerce')

# Convert Admission status based on the End Date and today's date
today = pd.Timestamp(datetime.date.today())
status_list = ['Active', 'In training','Admitted','Found Job']

mask = df['Admission Status'].isin(status_list) & (df['End Date'] < today)
df.loc[mask, 'Admission Status'] = 'Training Completed'

mask = df['Admission Status'].isin(status_list) & (df['End Date'] > today)
df.loc[mask, 'Admission Status'] = 'In Training'

# Convert CompTIA Drop out to Regular Drop out
df['Admission Status'] = df["Admission Status"].replace({'CompTIA - Incomplete/Drop out': 'Dropped Out'})

# Address null values
# Replace the Admission Batch column with the month extracted from the Admission Date column
df['Admission Batch'] = df['Admission Date'].dt.strftime('%B')

# Replace the null values of program column
df.fillna({'Program': 'Old Program'}, inplace=True);

# Replace null values and 0 or 1 values in the Package Amount column with 5000
df.loc[df['Package Amount'].isin([0, 1]) | df['Package Amount'].isna(), 'Package Amount'] = 5000

# Replace null values of Funding Source column
state_funding_map = {
    "Massachusetts": "WIOA - MA",
    "Pennsylvania": "WIOA - PA",
    "Vermont": "WIOA - VT",
    "New Hampshire": "WIOA - NH",
    "Rhode Island": "WIOA - RI",
    "Virginia": "WIOA - VA",
    "Florida": "WIOA - FL",
    "Maine": "WIOA - ME",
    "New York": "WIOA - NY",
    "New Jersey": "WIOA - NJ",
    "Maryland": "WIOA - MD",
    "Ohio": "WIOA - OH"
}

for state, funding in state_funding_map.items():
    df.loc[(df['Training Program Funding Source'].isnull()) & (df['State'] == state), 'Training Program Funding Source'] = funding

# Assign variables to represent the fiscal year end dates according to the corresponding years
end_2016 = pd.Timestamp(datetime.date(2016, 6, 30))
end_2017 = pd.Timestamp(datetime.date(2017, 6, 30))
end_2018 = pd.Timestamp(datetime.date(2018, 6, 30))
end_2019 = pd.Timestamp(datetime.date(2019, 6, 30))
end_2020 = pd.Timestamp(datetime.date(2020, 6, 30))
end_2021 = pd.Timestamp(datetime.date(2021, 6, 30))
end_2022 = pd.Timestamp(datetime.date(2022, 6, 30))
end_2023 = pd.Timestamp(datetime.date(2023, 6, 30))
end_2024 = pd.Timestamp(datetime.date(2024, 6, 30))
end_2025 = pd.Timestamp(datetime.date(2025, 6, 30))
end_2026 = pd.Timestamp(datetime.date(2026, 6, 30))

# Create a function that applies conditions to assign dates to their respective Fiscal Years
def fiscal_year(date):
    if date <= end_2016:
        return '2015'
    elif date <= end_2017:
        return '2016'
    elif date <= end_2018:
        return '2017'
    elif date <= end_2019:
        return '2018'
    elif date <= end_2020:
        return '2019'
    elif date <= end_2021:
        return '2020'
    elif date <= end_2022:
        return '2021'
    elif date <= end_2023:
        return '2022'
    elif date <= end_2024:
        return '2023'
    elif date <= end_2025:
        return '2024'
    elif date <= end_2026:
        return '2025'
    else:
        return '2026'


# Generate two columns for associating enrollment dates and end dates with a fiscal year
df['Enrolled FY'] = df['Start Date'].apply(fiscal_year)
df['Exited FY'] = df['End Date'].apply(fiscal_year)

# Add a new column to calculate the training duration in days
df["Training Duration Days"] = (pd.to_datetime(df["End Date"]) - pd.to_datetime(df["Start Date"])).dt.days

# Add a new column to calculate the number of days between inquiry and start
df["Inquiry To Start Days"] = (pd.to_datetime(df["Start Date"]) - pd.to_datetime(df["Inquiry Date"])).dt.days

# Add a new column to indicate whether the student has completed the training or not
df["Completed"] = (df["Admission Status"].str.lower().eq("training completed").astype(int))

# Add a new column to indicate whether the student has been placed or not
df["Placed"] = (df["Placement Information"].str.lower().eq("yes").astype(int))

# Save the data to an Excel file for additional analysis using Tableau
df.to_excel('data/cleaned/cleaned_data.xlsx', index=False)
df.to_csv('data/cleaned/cleaned_data.csv', index=False)
