import streamlit as st
import pandas as pd


# This function is used later
def lower(str):
    return str.lower()


# Title + File Uploader 
st.title("Merge DataSets")
files = st.file_uploader('Merge DataSets only use two files',accept_multiple_files=True)


if st.button("Submit", use_container_width=True):
    if len(files) == 2:
        st.success("Files Uploaded Correctly")
        for file in files:
            temp = pd.read_csv(file)
            if 'Timestamp' in temp:
                attend = temp
            else:
                ogSort = temp
        attend['Full Name']=attend['Full Name'].apply(lower)
        attend['WPI Email']=attend['WPI Email'].apply(lower)
        del ogSort['Unnamed: 0']

        st.write("This is the attendance form")
        st.write(attend)
        st.write("This is the orginal data")
        st.write(ogSort)
        event = attend['Event'].index[0]
        newMembers=[]
        for i in range(len(attend)):
            row=[]
            fullName=attend['Full Name'][i]
            email=attend['WPI Email'][i]

            print("This is the Email "+email)
            print("This is the ogSort "+ogSort['WPI Email'])
            print(email in ogSort['WPI Email'])

            if email in ogSort['WPI Email'].tolist():
                ogSort.loc[ogSort['WPI Email'] == email, 'Points'] += 1
                ogSort.loc[ogSort['WPI Email'] == email, 'Events Attended'] = ogSort.loc[ogSort['WPI Email'] == email, 'Events Attended'].str.cat(['newEvent'], sep=', ')
            else:
                newMembers.append(fullName)
                row.append(email)
                row.append(fullName)
                row.append(1)
                row.append(event)
                ogSort.loc[len(ogSort)] = row
        
        st.write("This is the merged data")
        st.write(ogSort)
        st.write("These are the new members")
        st.write(newMembers)
    else:
        st.error("You didn't put 2 files dumbass mf")

        

