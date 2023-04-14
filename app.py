import datetime
import streamlit as st

from src.heartrate_container import setUpHeartrateVisualizer
from src.sleep_container import setUpSleepVisualizer
from src.weight_container import setUpWeightVisualizer


if __name__ == '__main__':
    st.header("Fitness Band Data Visualiser")
    st.markdown("This is a demo visualiser which uses a fake dataset that mimics data from a Fitness Band. Currently the visualiser is only for Weight, Sleep and Heartrate data but it can be expanded to more data")
    st.markdown("Date available for dates: 04/12/2016 to 05/12/2016")
    d = st.date_input(label="Pick a date", value=datetime.date(2016, 5, 2))
    setUpHeartrateVisualizer(d)
    setUpWeightVisualizer(d)
    setUpSleepVisualizer(d)
