import streamlit as st
import pandas as pd
from utils.database import get_connection

conn = get_connection()

st.title("Executive Dashboard")

total_students = pd.read_sql("""
SELECT COUNT(*) AS Value
FROM training_data
""", conn)

completed = pd.read_sql("""
SELECT COUNT(*) AS Value
FROM training_data
WHERE Completed = 1
""", conn)

placed = pd.read_sql("""
SELECT COUNT(*) AS Value
FROM training_data
WHERE Placed = 1
""", conn)

revenue = pd.read_sql("""
SELECT SUM("Package Amount") AS Value
FROM training_data
""", conn)

c1, c2, c3, c4 = st.columns(4)

c1.metric("Students", int(total_students.iloc[0]["Value"]))
c2.metric("Completed", int(completed.iloc[0]["Value"]))
c3.metric("Placed", int(placed.iloc[0]["Value"]))
c4.metric("Revenue", f"${revenue.iloc[0]['Value']/1000000:,.2f}M")

st.subheader("State Performance")

state_df = pd.read_sql("""
SELECT *
FROM state_summary
ORDER BY TotalStudents DESC
""", conn)

st.dataframe(
    state_df,
    use_container_width=True
)

st.bar_chart(
    state_df.set_index("State")[["TotalStudents"]]
)

st.subheader("Enrollment Trend")

enrollment_df = pd.read_sql("""
SELECT
    "Academic Year",
    COUNT(*) AS Students
FROM training_data
GROUP BY "Academic Year"
ORDER BY "Academic Year"
""", conn)

st.line_chart(
    enrollment_df.set_index("Academic Year")
)

from datetime import datetime

st.caption(
    f"Last Refreshed: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
)