import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Data Dictionary",
    layout="wide"
)

st.title("📖 Data Dictionary")

st.markdown("""
This page describes the fields used in the Training Analytics database.
""")

data_dictionary = pd.DataFrame({

    "Field": [
        "Program",
        "Gender",
        "Academic Year",
        "Inquiry Date",
        "Admission Batch",
        "Training Program Funding Source",
        "Admission Date",
        "Start Date",
        "End Date",
        "Admission Status",
        "Lead Source",
        "Coordinator",
        "Grand Total",
        "Lead Stage",
        "Package Amount",
        "Placement Information",
        "Placement Salary Range",
        "Placement Job Title",
        "State",
        "Placement Employer",
        "Placement Remark",
        "Uploaded Documents",
        "Assigned Career center",
        "Enrolled FY",
        "Exited FY",
        "Training Duration Days",
        "Inquiry To Start Days",
        "Completed",
        "Placed"
    ],

    "Description": [
        "Training program selected by the student.",
        "Student gender.",
        "Academic year of enrollment.",
        "Date of first inquiry.",
        "Student admission batch.",
        "Source funding the training program.",
        "Student admission date.",
        "Training start date.",
        "Training end date.",
        "Current admission or training status.",
        "Source of the student lead.",
        "Coordinator managing the student.",
        "Total amount associated with the student record.",
        "Current lead stage.",
        "Program tuition or package amount.",
        "Indicates if student obtained placement.",
        "Salary range after placement.",
        "Job title obtained after placement.",
        "State associated with the student.",
        "Employer where student was placed.",
        "Additional placement notes.",
        "Documents uploaded by student.",
        "Assigned workforce or career center.",
        "Fiscal year of enrollment.",
        "Fiscal year of exit.",
        "Calculated training duration in days.",
        "Days between inquiry and training start.",
        "Completion indicator (1 = Completed, 0 = Not Completed).",
        "Placement indicator (1 = Placed, 0 = Not Placed)."
    ]
})

st.dataframe(
    data_dictionary,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

st.subheader("Key Business Metrics")

metrics_df = pd.DataFrame({
    "Metric": [
        "Completion Rate",
        "Placement Rate",
        "Training Duration",
        "Inquiry To Start Time",
        "Program Revenue"
    ],
    "Definition": [
        "Percentage of students with Completed = 1",
        "Percentage of students with Placed = 1",
        "Average Training Duration Days",
        "Average Inquiry To Start Days",
        "Sum of Package Amount"
    ]
})

st.dataframe(
    metrics_df,
    use_container_width=True,
    hide_index=True
)

st.success(
    "This data dictionary documents all fields available in the training_data table."
)

from datetime import datetime

st.caption(
    f"Last Refreshed: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
)