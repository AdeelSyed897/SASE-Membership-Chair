import streamlit as st
import pandas as pd

st.set_page_config(layout="centered")

# This function is used later
def lower(str):
    return str.lower()

# Title and file uploader
st.title("Creating The Dataset")
file = st.file_uploader('Create DataSet',accept_multiple_files=False)



# Need the if statement for error handling
if file is not None:
    # Creating the Sorted Data Frame
    newDf= pd.DataFrame(columns=['WPI Email', 'Name', 'Points', 'Events Attended'])

    # Reading in the uploaded file
    df = pd.read_csv(file)

    # Error handeling to help people who sometimes capitlize their email / name
    df['Full Name']=df['Full Name'].apply(lower)
    df['WPI Email']=df['WPI Email'].apply(lower)
    st.write(df)
    visited=[]

    # Loops through the attendace form
    for i in range(len(df)):
        row=[]
        events=[]
        fullName=df['Full Name'][i]
        email=df['WPI Email'][i]

        # If you have already added the row skip the occurrence 
        if email in visited:
            continue

        # Filter Dataset with only occurrences of the member's email
        filteredEmail = df[df['WPI Email'] == email]

        # len of filtered df is how many events they attended
        points=len(filteredEmail)
        events=filteredEmail['Event'].tolist()
        visited.append(email)
        row.append(email)
        row.append(fullName)
        row.append(points)
        row.append(events)
        
        #adding the row to the df
        newDf.loc[len(newDf)] = row
    st.write(newDf)
else:
    st.write("Enter Data")

