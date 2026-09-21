from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


# ============================================================
# STUDENT RESPONSE MODEL
# ============================================================

class StudentCountResponse(BaseModel):
    total_students: int


# ============================================================
# PROGRAM MODELS
# ============================================================

class ProgramSummaryResponse(BaseModel):
    Program: Optional[str] = None
    TotalStudents: int
    CompletionRate: Optional[float] = None
    PlacementRate: Optional[float] = None
    Revenue: Optional[float] = None
    AvgTrainingDays: Optional[float] = None


class ProgramRequest(BaseModel):
    program: str = Field(
        ...,
        min_length=1,
        description="Full or partial program name"
    )


class ProgramSearchResponse(BaseModel):
    search_term: str
    match_count: int
    programs: List[ProgramSummaryResponse]


class ProgramListResponse(BaseModel):
    count: int
    programs: List[ProgramSummaryResponse]


# ============================================================
# STATE RESPONSE MODEL
# ============================================================

class StateSummaryResponse(BaseModel):
    State: Optional[str] = None
    TotalStudents: int
    CompletionRate: Optional[float] = None
    PlacementRate: Optional[float] = None


# ============================================================
# FUNDING RESPONSE MODEL
# ============================================================

class FundingSummaryResponse(BaseModel):
    FundingSource: Optional[str] = None
    TotalStudents: int
    CompletionRate: Optional[float] = None
    PlacementRate: Optional[float] = None
    Revenue: Optional[float] = None


# ============================================================
# QUESTION MODELS
# ============================================================

class QuestionRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        description="Business question about the training data"
    )


class QuestionResponse(BaseModel):
    question: str
    result_count: int
    results: List[Dict[str, Any]]


# ===============================