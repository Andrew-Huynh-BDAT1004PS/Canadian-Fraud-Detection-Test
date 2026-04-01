# %%
#andrew https://docs.google.com/document/d/1hA5mRtAiVFTnJYx3Y591MG3zVfPzRPDAdXCp0hxPiog/edit?tab=t.0

# %%
#%pip install pandas

import pandas as pd
df = pd.read_csv(r"cafc-open-gouv-database-2021-01-01-to-2025-09-30-extracted-2025-10-01.csv")

print(df)

# %%
# Data Cleaning

#Rename column names, removing the French and keeping the English
df.rename(columns={
    "Date Received / Date reçue": "Date",
    "Numéro d'identification / Number ID": "ID",
    "Victim Age Range / Tranche d'âge des victimes": "Age Range",
    "Number of Victims / Nombre de victimes": "Victims",
    "Dollar Loss /pertes financières": "Loss"
}, inplace=True)

print(df.head())

#Drop all columns containing information only in French
df= df.drop(
    [
      'Type de plainte reçue',
     'Pays',
     'Catégories thématiques sur la fraude et la cybercriminalité',
     'Méthode de sollicitation',
     'Langue de correspondance',
     'Type de plainte',
     ]
    , axis='columns')

print(df.head())


#Drop apostrophe in  Age Range Column
df["Age Range"] = df["Age Range"].str[1:].fillna(df["Age Range"])

print(df["Age Range"].head())


#Remove $ and Comma  in the loss Column
df['Loss'] = df['Loss'].astype(str).str.replace('$', '', regex=False).str.replace(',', '', regex=False)
#Convert the Loss column to floating data type/numeric, coercing errors to NaN, and then fill NaN with 0
df['Loss'] = pd.to_numeric(df['Loss']).fillna(0) 

print(df['Loss'].dtype)
print(df['Loss'].head())

#Convert the Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])
print(df["Date"])

#Check for null values in the dataset
print(df.isnull().sum())

total_nulls = df.isnull().sum().sum()
print("There are " + str(total_nulls) + " null values in the dataset.")

# %%
# Data Visualization
#NOTES: Convert/copy file from .ipynb to .py before deploying on GitHub, which is required for StreamLit
#%pip install streamlit_jupyter

import streamlit as st

 
st.write("Dataset Preview")
st.dataframe(df.head())

# %%


