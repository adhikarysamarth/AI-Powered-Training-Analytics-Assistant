import streamlit as st
import pandas as pd
from utils.database import get_connection

conn = get_connection()

st.title("Program Analytics")

# ----------------------------------------
# Program Summary
# ----------------------------------------

#program_df = pd.read_sql("""
#SELECT *
#FROM program_summary
#ORDER BY TotalStudents DESC
#""", conn)

from utils.api_client import get_program_summary

program_df = pd.DataFrame(get_program_summary())

st.subheader("Program Performance Summary")

st.dataframe(
    program_df,
    use_container_width=True
)

# ----------------------------------------
# Download Button
# ----------------------------------------

csv = program_df.to_csv(index=False)

st.download_button(
    label="Download Program Summary",
    data=csv,
    file_name="program_summary.csv",
    mime="text/csv"
)

# ----------------------------------------
# Students by Program
# ----------------------------------------

st.subheader("Students by Program")

st.bar_chart(
    program_df.set_index("Program")[["TotalStudents"]]
)

# ----------------------------------------
# Completion Rate by Program
# ----------------------------------------

st.subheader("Completion Rate by Program")

completion_chart = program_df[
    ["Program", "CompletionRate"]
]

st.bar_chart(
    completion_chart.set_index("Program")
)

# ----------------------------------------
# Placement Rate by Program
# ----------------------------------------

st.subheader("Placement Rate by Program")

placement_chart = program_df[
    ["Program", "PlacementRate"]
]

st.bar_chart(
    placement_chart.set_index("Program")
)

# ----------------------------------------
# Revenue by Program
# ----------------------------------------

st.subheader("Revenue by Program")

revenue_chart = program_df[
    ["Program", "Revenue"]
]

st.bar_chart(
    revenue_chart.set_index("Program")
)

# ----------------------------------------
# Average Training Duration
# ----------------------------------------

st.subheader("Average Training Days by Program")

duration_chart = program_df[
    ["Program", "AvgTrainingDays"]
]

st.bar_chart(
    duration_chart.set_index("Program")
)

csv = program_df.to_csv(index=False)

st.download_button(
    "Download Program Analytics",
    csv,
    "program_analytics.csv",
    "text/csv"
)

from datetime import datetime

st.caption(
    f"Last Refreshed: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
)