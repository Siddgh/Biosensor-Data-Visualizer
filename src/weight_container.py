import streamlit as st
import pandas as pd


def setUpWeightVisualizer(d):
    weight_data_raw_df = pd.read_csv('data/weightLogInfo_merged.csv')
    weight_data_raw_df['Date'] = pd.to_datetime(
        weight_data_raw_df['Date'])
    weight_data_raw_df['Date Month'] = weight_data_raw_df['Date'].dt.month
    weight_data_raw_df['Date Day'] = weight_data_raw_df['Date'].dt.day

    weightVisualizer = st.container()

    with weightVisualizer:
        st.title("Weight / BMI Visualizer")
        st.text("Weight Data is collected from a mock dataset from a Fitbit Device")

        weightChartsDisplayFor = st.selectbox(
            'Display Charts for', ['Weight', 'BMI'])

        weightDfForSpecificMonth = weight_data_raw_df[weight_data_raw_df['Date Month'] == d.month]
        if weightDfForSpecificMonth.size != 0:
            if weightChartsDisplayFor == "Weight":
                weightDisplayType = st.radio(
                    'Display Weight in:', ['Kg', 'Pounds'])
                if weightDisplayType == 'Kg':
                    st.line_chart(weightDfForSpecificMonth,
                                  x='Date Day', y='WeightKg')
                    st.write(weightDfForSpecificMonth[[
                        'Id', 'Date', 'WeightKg', 'Fat', 'BMI', 'LogId']])
                else:
                    st.line_chart(weightDfForSpecificMonth,
                                  x='Date Day', y='WeightPounds')
                    st.write(weightDfForSpecificMonth[[
                        'Id', 'Date', 'WeightPounds', 'Fat', 'BMI', 'LogId']])
            else:
                st.line_chart(weightDfForSpecificMonth, x='Date Day',
                              y='BMI')
                st.write(weightDfForSpecificMonth[[
                    'Id', 'Date', 'WeightKg', 'WeightPounds', 'Fat', 'BMI', 'LogId']])
        else:
            st.error("No Data Found")
