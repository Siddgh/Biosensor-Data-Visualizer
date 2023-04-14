import streamlit as st
import pandas as pd


@staticmethod
def setUpHeartrateVisualizer(d):
    heartrate_data_raw_df = pd.read_csv('data/heartrate_seconds_merged.csv')
    date_list = str(d).split('-')

    date_to_search = '%d/%d/%d' % (int(date_list[1]),
                                   int(date_list[2]), int(date_list[0]))

    heartRateVisualizer = st.container()

    filtered_heartrate_dataframe = heartrate_data_raw_df[heartrate_data_raw_df['Time'].str.contains(
        date_to_search)]

    filtered_heartrate_dataframe["Time HHMMSS"] = filtered_heartrate_dataframe["Time"].str.split(
        " ").str.get(1) + " " + filtered_heartrate_dataframe["Time"].str.split(
        " ").str.get(2)

    with heartRateVisualizer:
        st.title("Heart Rate Visualizer")
        heartrate_sample_value = st.selectbox('Time', ['ALL', 'AM', 'PM'])

        if heartrate_sample_value == "AM":
            filtered_heartrate_dataframe = filtered_heartrate_dataframe[filtered_heartrate_dataframe['Time HHMMSS'].str.contains(
                "AM")]
        elif heartrate_sample_value == "PM":
            filtered_heartrate_dataframe = filtered_heartrate_dataframe[filtered_heartrate_dataframe['Time HHMMSS'].str.contains(
                "PM")]

        st.line_chart(filtered_heartrate_dataframe, x='Time HHMMSS', y='Value')
        st.text("Total Records : " + str(filtered_heartrate_dataframe.size))
        st.write(filtered_heartrate_dataframe.sort_values(
            by='Time', ascending=True))
