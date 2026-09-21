from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from api.database import get_connection
from utils.sql_resolver import resolve_question

app = FastAPI(
    title="Training Analytics API",
    description="API for training enrollment and outcome analytics",
    version="1.0.0"
)

def rows_to_dicts(cursor, rows):
    column_names = []

    for column in cursor.description:
        column_names.append(column[0])

    results = []

    for row in rows:
        record = dict(zip(column_names, row))
        results.append(record)

    return results

class StudentRequest(BaseModel):
    program: str
    state: str

class ProgramRequest(BaseModel):
    program: str

class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def home():

    return {
        "application": "Training Analytics API",
        "status": "running"
    }


@app.get("/students")
def students():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(Program)
        FROM training_data
        """
    )

    total = cursor.fetchone()[0]

    conn.close()

    return {
        "total_students": total
    }

@app.get("/program_summary")
def program_summary():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM program_summary
    ORDER BY TotalStudents DESC
    """)

    columns = [
        column[0]
        for column in cursor.description
    ]

    rows = cursor.fetchall()

    result = [
        dict(zip(columns, row))
        for row in rows
    ]

    conn.close()

    return result

@app.get("/state_summary")
def state_summary():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM state_summary
    ORDER BY TotalStudents DESC
    """)

    columns = [
        column[0]
        for column in cursor.description
    ]

    rows = cursor.fetchall()

    result = [
        dict(zip(columns, row))
        for row in rows
    ]

    conn.close()

    return result

@app.get("/funding_summary")
def funding_summary():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM funding_summary
    ORDER BY TotalStudents DESC
    """)

    columns = [
        column[0]
        for column in cursor.description
    ]

    rows = cursor.fetchall()

    result = [
        dict(zip(columns, row))
        for row in rows
    ]

    conn.close()

    return result


##### POST Endpoint

@app.post("/analyze")
def analyze_student(request: StudentRequest):

    return {
        "program": request.program,
        "state": request.state,
        "message": "Request received successfully"
    }

@app.post("/program_details")
def program_details(request: ProgramRequest):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            Program,
            TotalStudents,
            CompletionRate,
            PlacementRate,
            Revenue,
            AvgTrainingDays
        FROM program_summary
        WHERE LOWER(TRIM(Program)) LIKE LOWER(?)
        ORDER BY TotalStudents DESC
        """,
        (f"%{request.program.strip()}%",)
    )

    rows = cursor.fetchall()

    if not rows:
        conn.close()

        raise HTTPException(
            status_code=404,
            detail=f"No program found containing '{request.program}'"
        )

    column_names = [
        column[0]
        for column in cursor.description
    ]

    results = [
        dict(zip(column_names, row))
        for row in rows
    ]

    conn.close()

    return {
        "search_term": request.program,
        "match_count": len(results),
        "programs": results
    }

@app.post("/question")
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

        column_names = [
            column[0]
            for column in cursor.description
        ]

        results = [
            dict(zip(column_names, row))
            for row in rows
        ]

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Database query failed: {str(error)}"
        )

    finally:
        conn.close()

    return {
        "question": question,
        "result_count": len(results),
        "results": results
    }