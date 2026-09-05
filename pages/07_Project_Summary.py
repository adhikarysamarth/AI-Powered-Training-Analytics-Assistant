import streamlit as st

st.title("Project Summary")

st.markdown("""
## AI-Powered Training Analytics Assistant

This project was built to analyze:

- Student Enrollment
- Program Performance
- Completion Outcomes
- Job Placement Outcomes
- Funding Source Utilization

### Data Pipeline

Excel
→ Python Cleaning
→ SQLite Database
→ SQL Analytics
→ Streamlit Dashboard
→ Natural Language Queries

## Project Statistics

- 9,000+ Student Records
- Multiple Training Programs
- Multiple States
- Placement Analytics
- Funding Analytics
- Career Center Analytics
- Natural Language Query Assistant

### Business Questions Answered

- How many students enrolled?
- Which programs perform best?
- What is the placement rate?
- Which employers hire students?
- Which funding sources are most effective?
""")

from datetime import datetime

st.caption(
    f"Last Refreshed: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
)