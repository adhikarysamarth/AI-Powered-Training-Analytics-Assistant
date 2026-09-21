import streamlit as st
import pandas as pd
import requests

from utils.api_client import ask_question

st.set_page_config(
    page_title="AI Assistant",
    layout="wide"
)

st.title("AI Assistant")

st.info(
    """
    AI Assistant Beta

    The current version maps supported business questions to SQL queries
    through the FastAPI backend.

    Example questions:

    - total students
    - placement rate
    - completion rate
    - students by state
    - funding source
    """
)

question = st.text_input(
    "Ask a question about the training data"
)

submit_button = st.button(
    "Submit Question",
    type="primary"
)

if submit_button:

    if not question.strip():

        st.warning(
            "Please enter a question."
        )

    else:

        try:

            with st.spinner(
                "Retrieving analytics..."
            ):

                api_response = ask_question(
                    question.strip()
                )

            results = api_response.get(
                "results",
                []
            )

            st.success(
                "Question processed successfully."
            )

            st.write(
                f"Question: {api_response.get('question')}"
            )

            st.write(
                f"Rows returned: {api_response.get('result_count', 0)}"
            )

            if results:

                result_df = pd.DataFrame(
                    results
                )

                st.dataframe(
                    result_df,
                    use_container_width=True,
                    hide_index=True
                )

                if len(result_df.columns) == 2:

                    first_column = result_df.columns[0]
                    second_column = result_df.columns[1]

                    if pd.api.types.is_numeric_dtype(
                        result_df[second_column]
                    ):

                        chart_df = result_df.set_index(
                            first_column
                        )

                        st.bar_chart(
                            chart_df
                        )

                csv_data = result_df.to_csv(
                    index=False
                )

                st.download_button(
                    label="Download Results",
                    data=csv_data,
                    file_name="analytics_results.csv",
                    mime="text/csv"
                )

            else:

                st.info(
                    "The query ran successfully but returned no records."
                )

        except requests.exceptions.ConnectionError:

            st.error(
                """
                The FastAPI backend is not running.

                Open a second Terminal window and run:

                python3 -m uvicorn api.main:app --reload
                """
            )

        except requests.exceptions.HTTPError as error:

            error_message = "The API could not process the question."

            try:

                error_response = error.response.json()

                error_message = error_response.get(
                    "detail",
                    error_message
                )

            except ValueError:

                pass

            st.error(
                error_message
            )

        except requests.exceptions.Timeout:

            st.error(
                "The API request took too long. Please try again."
            )

        except Exception as error:

            st.error(
                f"Unexpected error: {str(error)}"
            )

st.markdown("---")

st.caption(
    "Training Analytics Assistant | Streamlit + FastAPI + SQLite"
)