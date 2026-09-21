import streamlit as st
import pandas as pd
from utils.database import get_connection
from utils.sql_resolver import resolve_question

conn = get_connection()

st.title("AI Assistant")

question = st.text_input(
    "Ask a question"
)

if question:

    sql = resolve_question(question)

    if sql:

        result = pd.read_sql(
            sql,
            conn
        )

        st.dataframe(
            result,
            use_container_width=True
        )

    else:

        st.warning(
            "Question not recognized."
        )

from datetime import datetime

st.caption(
    f"Last Refreshed: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
)

st.markdown("""
### Sample Questions

- total students
- placement rate
- completion rate
- students by state
- top employers
- largest program
- largest state
- revenue by program
- placement by state
- completion by state
""")