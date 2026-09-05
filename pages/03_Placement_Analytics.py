import streamlit as st
import pandas as pd
from utils.database import get_connection

conn = get_connection()

st.title("Placement Analytics")

placement_df = pd.read_sql("""
SELECT
    Program,
    PlacementRate
FROM program_summary
ORDER BY PlacementRate DESC
""", conn)

st.subheader("Placement Rate by Program")

st.dataframe(
    placement_df,
    use_container_width=True
)

st.bar_chart(
    placement_df.set_index("Program")
)

st.subheader("Top Employers")

employer_df = pd.read_sql("""
SELECT
    "Placement Employer" AS Employer,
    COUNT(*) AS Hires
FROM training_data
WHERE Placed = 1
GROUP BY "Placement Employer"
ORDER BY Hires DESC
LIMIT 10
""", conn)

st.dataframe(
    employer_df,
    use_container_width=True
)

st.subheader("Salary Distribution")

salary_df = pd.read_sql("""
SELECT
    "Placement Salary Range" AS SalaryRange,
    COUNT(*) AS Students
FROM training_data
WHERE Placed = 1
GROUP BY "Placement Salary Range"
ORDER BY Students DESC
""", conn)

st.dataframe(
    salary_df,
    use_container_width=True
)

csv = placement_df.to_csv(index=False)

st.download_button(
    "Download Placement Analytics",
    csv,
    "placement_analytics.csv",
    "text/csv"
)

from datetime import datetime

st.caption(
    f"Last Refreshed: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
)