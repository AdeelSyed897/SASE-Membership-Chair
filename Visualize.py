import streamlit as st
import pandas as pd
import statistics

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
    

    del bars['Exec']
    for i in bars:
        bars[i]+=8
    barData = pd.DataFrame(list(bars.items()),columns=["Event", "Attendees"])
    barsData = barData.set_index("Event",inplace=True)
    st.bar_chart(barData,horizontal=True)

    a, b = st.columns(2)
    c, d = st.columns(2)

    #calculate the mean
    values = list(bars.values())
    mean = statistics.mean(values)
    a.metric("Mean Attendance", mean)

    #calculate the median
    median = statistics.median(values)
    b.metric("Median Attendance", median)

    #Max attended event
    maxEvent = max(bars, key=bars.get)
    maxAttendees = bars[maxEvent]
    c.metric("Max attended event: "+maxEvent, maxAttendees)

    #Min attended event
    minEvent = min(bars, key=bars.get)
    minAttendees = bars[minEvent]
    d.metric("Min attended event: "+minEvent, minAttendees)

 







