import streamlit as st
import pandas as pd

st.title("Visualize Data")

# Title and file uploader
st.title("Visualizing The Data")
file = st.file_uploader('Visualize DataSet',accept_multiple_files=False)



# Need the if statement for error handling
if file is not None:

    # Reading in the uploaded file
    df = pd.read_csv(file)

    bars={}
    visited=[]
    for i in range(len(df)):
        eventsStr = df['Events Attended'][i]
        events = eventsStr.split(',')
        for event in events:
            if event not in visited:
                visited.append(event)
                bars[event]=1
            else:
                bars[event]+=1
    
    barData = pd.DataFrame(list(bars.items()),columns=["Event", "Attendees"])
    barsData = barData.set_index("Event",inplace=True)

    print(barData)
    st.bar_chart(barData,horizontal=True)







