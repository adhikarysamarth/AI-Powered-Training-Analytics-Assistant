from fastapi import FastAPI, HTTPException, Query

from api.database import get_connection
from api.models import (
    FundingSummaryResponse,
    ProgramRequest,
    ProgramSearchResponse,
    ProgramSummaryResponse,
    QuestionRequest,
    QuestionResponse,
    StateSummaryResponse,
    StudentCountResponse,
)

from utils.sql_resolver import resolve_question

app = FastAPI(
    title="Training Analytics API",
    description="API for training enrollment and outcome analytics",
    version="1.0.0"
)


# ============================================================
# HELPER FUNCTION
# ============================================================

def rows_to_dicts(cursor, rows):

    column_names = [
        column[0]
        for column in cursor.description
    ]

    return [
        dict(zip(column_names, row))
        for row in rows
    ]


# ============================================================
# HOME
# ============================================================

@app.get("/")
def home():

    return {
        "application": "Training Analytics API",
        "status": "running"
    }


# ============================================================
# STUDENTS
# ============================================================

@app.get(
    "/students",
    response_model=StudentCountResponse
)
def get_students():

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
        SELECT COUNT(*)
        FROM training_data
        """)

        total_students = cursor.fetchone()[0]

        return {
            "total_students": total_students
        }

    finally:

        conn.close()


# ============================================================
# PROGRAM SUMMARY
# ============================================================

@app.get(
    "/program_summary",
    response_model=list[ProgramSummaryResponse]
)
def get_program_summary():

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
        SELECT *
        FROM program_summary
        ORDER BY TotalStudents DESC
        """)

        rows = cursor.fetchall()

        return rows_to_dicts(
            cursor,
            rows
        )

    finally:

        conn.close()


# ============================================================
# STATE SUMMARY
# ============================================================

@app.get(
    "/state_summary",
    response_model=list[StateSummaryResponse]
)
def get_state_summary():

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
        SELECT *
        FROM state_summary
        ORDER BY TotalStudents DESC
        """)

        rows = cursor.fetchall()

        return rows_to_dicts(
            cursor,
            rows
        )

    finally:

        conn.close()


# ============================================================
# FUNDING SUMMARY
# ============================================================

@app.get(
    "/funding_summary",
    response_model=list[FundingSummaryResponse]
)
def get_funding_summary():

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
        SELECT *
        FROM funding_summary
        ORDER BY TotalStudents DESC
        """)

        rows = cursor.fetchall()

        return rows_to_dicts(
            cursor,
            rows
        )

    finally:

        conn.close()


# ============================================================
# TOP PROGRAMS
# ============================================================

@app.get("/programs")
def get_programs(

    limit: int = Query(
        default=10,
        ge=1,
        le=100
    )

):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
        SELECT
            Program,
            TotalStudents,
            CompletionRate,
            PlacementRate,
            Revenue,
            AvgTrainingDays
        FROM program_summary
        ORDER BY TotalStudents DESC
        LIMIT ?
        """,
        (limit,)
        )

        rows = cursor.fetchall()

        return {
            "count": len(rows),
            "programs": rows_to_dicts(
                cursor,
                rows
            )
        }

    finally:

        conn.close()


# ============================================================
# PROGRAM SEARCH
# ============================================================

@app.get("/program/{program_name}")
def get_program(program_name: str):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
        SELECT
            Program,
            TotalStudents,
            CompletionRate,
            PlacementRate,
            Revenue,
            AvgTrainingDays
        FROM program_summary
        WHERE LOWER(TRIM(Program))
              LIKE LOWER(?)
        """,
        (f"%{program_name.strip()}%",)
        )

        rows = cursor.fetchall()

        if not rows:

            raise HTTPException(
                status_code=404,
                detail="Program not found"
            )

        return {
            "search_term": program_name,
            "match_count": len(rows),
            "programs": rows_to_dicts(
                cursor,
                rows
            )
        }

    finally:

        conn.close()


# ============================================================
# PROGRAM DETAILS POST
# ============================================================

@app.post(
    "/program_details",
    response_model=ProgramSearchResponse
)
def program_details(request: ProgramRequest):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
        SELECT
            Program,
            TotalStudents,
            CompletionRate,
            PlacementRate,
            Revenue,
            AvgTrainingDays
        FROM program_summary
        WHERE LOWER(TRIM(Program))
              LIKE LOWER(?)
        ORDER BY TotalStudents DESC
        """,
        (f"%{request.program.strip()}%",)
        )

        rows = cursor.fetchall()

        if not rows:

            raise HTTPException(
                status_code=404,
                detail=f"No program found containing '{request.program}'"
            )

        results = rows_to_dicts(
            cursor,
            rows
        )

        return {
            "search_term": request.program,
            "match_count": len(results),
            "programs": results
        }

    finally:

        conn.close()


# ============================================================
# ANALYTICS QUESTION
# ============================================================

@app.post(
    "/question",
    response_model=QuestionResponse
)
def answer_question(request: QuestionRequest):

    question = request.question.strip()

    if not question:

        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty"
        )

    sql_query = resolve_question(question)

    if sql_query is None:

        raise HTTPException(
            status_code=400,
            detail="Question is not currently supported"
        )

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(sql_query)

        rows = cursor.fetchall()

        results = rows_to_dicts(
            cursor,
            rows
        )

        return {
            "question": question,
            "result_count": len(results),
            "results": results
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Database query failed: {str(error)}"
        )

    finally:

        conn.close()