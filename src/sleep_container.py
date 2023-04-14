import streamlit as st
import pandas as pd


@staticmethod
def setUpSleepVisualizer(d):
    sleep_data_raw_df = pd.read_csv('data/sleepDay_merged.csv')
    sleep_data_raw_df['SleepDay'] = pd.to_datetime(
        sleep_data_raw_df['SleepDay'])
    sleep_data_raw_df['Date Month'] = sleep_data_raw_df['SleepDay'].dt.month
    sleep_data_raw_df['Date Day'] = sleep_data_raw_df['SleepDay'].dt.day

    sleepVisualizer = st.container()

    with sleepVisualizer:
        st.title("Sleep Visualizer")

        sleepDfForSpecificMonth = sleep_data_raw_df[sleep_data_raw_df['Date Month'] == d.month]
        if sleepDfForSpecificMonth.size != 0:
            st.subheader("Total Number of Naps in a Day")
            st.bar_chart(sleepDfForSpecificMonth, x="Date Day",
                         y="TotalSleepRecords")
            st.subheader("Total Time in Bed vs Total Time Asleep")
            st.area_chart(sleepDfForSpecificMonth, x="Date Day", y=[
                          "TotalMinutesAsleep", "TotalTimeInBed"])
            st.write(sleepDfForSpecificMonth[['Id', 'SleepDay',
                     'TotalSleepRecords', 'TotalMinutesAsleep', 'TotalTimeInBed']])

        else:
            st.error("No Data Found")
