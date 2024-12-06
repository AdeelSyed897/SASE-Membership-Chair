import streamlit as st
import pandas as pd


# This function is used later
def lower(str):
    return str.lower()


# Title + File Uploader 
st.title("Merge DataSets")
files = st.file_uploader('Merge DataSets only use two files',accept_multiple_files=True)

# Once button is clicked then do all the code
if st.button("Submit", use_container_width=True):

    # Only Take two Files
    if len(files) == 2:
        st.success("Files Uploaded Correctly")

        # Reading the Files
        for file in files:
            temp = pd.read_csv(file)
            if 'Timestamp' in temp:
                attend = temp
            else:
                ogSort = temp
        
        # Changing everthing to lowercase for conciseness
        attend['Full Name']=attend['Full Name'].apply(lower)
        attend['WPI Email']=attend['WPI Email'].apply(lower)
        del ogSort['Unnamed: 0']

        # Display the data
        st.write("This is the attendance form")
        st.write(attend)
        st.write("This is the orginal data")
        st.write(ogSort)

        # Set the Event 
        event = attend['Event'].index[0]
        newMembers=[]
        for i in range(len(attend)):
            # Creating the values
            row=[]
            fullName=attend['Full Name'][i]
            email=attend['WPI Email'][i]
            
            # If the Member exists update with data
            if email in ogSort['WPI Email'].tolist():
                ogSort.loc[ogSort['WPI Email'] == email, 'Points'] += 1
                ogSort.loc[ogSort['WPI Email'] == email, 'Events Attended'] = ogSort.loc[ogSort['WPI Email'] == email, 'Events Attended'].str.cat([str(event)], sep=', ')
            # If its a New Member create a new row and add to the new members list
            else:
                newMembers.append(fullName)
                row.append(email)
                row.append(fullName)
                row.append(1)
                row.append(event)
                ogSort.loc[len(ogSort)] = row
        # Display the New Data and New Members
        st.write("This is the merged data")
        st.write(ogSort)
        st.write("These are the new members")
        st.write(newMembers)
    else:
        st.error("You didn't put 2 files dumbass mf")

        

