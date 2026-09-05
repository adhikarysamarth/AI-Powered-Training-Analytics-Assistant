import streamlit as st
import pandas as pd
from utils.database import get_connection

conn = get_connection()

st.title("Career Center Analytics")

career_df = pd.read_sql("""
SELECT *
FROM career_center_summary
ORDER BY TotalStudents DESC
""", conn)

st.subheader("Career Center Performance")

st.dataframe(
    career_df,
    use_container_width=True
)

st.bar_chart(
    career_df.set_index("CareerCenter")[["TotalStudents"]]
)

st.subheader("Coordinator Performance")

coordinator_df = pd.read_sql("""
SELECT *
FROM coordinator_summary
ORDER BY TotalStudents DESC
""", conn)

st.dataframe(
    coordinator_df,
    use_container_width=True
)

st.bar_chart(
    coordinator_df.set_index("Coordinator")[["TotalStudents"]]
)

csv = career_df.to_csv(index=False)

st.download_button(
    "Download Career Center Analytics",
    csv,
    "career_center_analytics.csv",
    "text/csv"
)

from datetime import datetime

st.caption(
    f"Last Refreshed: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
)