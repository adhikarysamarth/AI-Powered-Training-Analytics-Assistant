import streamlit as st
import pandas as pd
from utils.database import get_connection

conn = get_connection()

st.title("Funding Analytics")

funding_df = pd.read_sql("""
SELECT *
FROM funding_summary
ORDER BY TotalStudents DESC
""", conn)

st.subheader("Funding Source Performance")

st.dataframe(
    funding_df,
    use_container_width=True
)

st.subheader("Students by Funding Source")

st.bar_chart(
    funding_df.set_index("FundingSource")[["TotalStudents"]]
)

st.subheader("Completion Rate by Funding Source")

st.bar_chart(
    funding_df.set_index("FundingSource")[["CompletionRate"]]
)

st.subheader("Placement Rate by Funding Source")

st.bar_chart(
    funding_df.set_index("FundingSource")[["PlacementRate"]]
)

st.subheader("Revenue by Funding Source")

st.bar_chart(
    funding_df.set_index("FundingSource")[["Revenue"]]
)

csv = funding_df.to_csv(index=False)

st.download_button(
    "Download Funding Analytics",
    csv,
    "funding_analytics.csv",
    "text/csv"
)

from datetime import datetime

st.caption(
    f"Last Refreshed: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
)