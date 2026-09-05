import streamlit as st

st.set_page_config(
    page_title="AI-Powered Training Analytics Assistant",
    layout="wide"
)

st.title("🏠 AI-Powered Training Analytics Assistant")

import streamlit as st
import pandas as pd
from utils.database import get_connection

conn = get_connection()

students = pd.read_sql("""
SELECT COUNT(*) AS Value
FROM training_data
""", conn)

programs = pd.read_sql("""
SELECT COUNT(DISTINCT Program) AS Value
FROM training_data
""", conn)

states = pd.read_sql("""
SELECT COUNT(DISTINCT State) AS Value
FROM training_data
""", conn)

st.markdown("""
## Welcome

This application analyzes student training outcomes, placements, program performance, funding sources, and career center effectiveness.

### Navigate Using the Sidebar

📊 Executive Dashboard

🎓 Program Analytics

💼 Placement Analytics

💰 Funding Analytics

🏢 Career Center Analytics

🤖 AI Assistant

📖 Data Dictionary

📋 Project Summary

---

### Technology Stack

- Python
- Pandas
- SQLite
- SQL
- Streamlit

### Data Pipeline
```text
Excel Data
↓
Python Data Cleaning
↓
SQLite Database
↓
Analytics Views
↓
Interactive Dashboard
↓
Natural Language Analytics
""")

