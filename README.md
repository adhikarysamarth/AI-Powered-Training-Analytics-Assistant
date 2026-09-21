> Version 1.0 currently includes a complete analytics platform featuring interactive dashboards, SQL-driven insights, a FastAPI backend, and a natural-language query interface.
>
> Future releases will incorporate Azure OpenAI, natural-language-to-SQL generation, AI-powered insights, Retrieval-Augmented Generation (RAG), and Azure cloud deployment.

# AI-Powered Training Analytics Assistant

## Project Overview

The AI-Powered Training Analytics Assistant is an end-to-end analytics platform designed to transform student training and placement data into actionable business insights.

The application combines data engineering, SQL analytics, interactive dashboards, business intelligence reporting, and a natural-language query interface to help users analyze:

- Student Enrollment
- Program Performance
- Training Completion
- Employment Placement
- Funding Source Performance
- Career Center Outcomes

The project began as a traditional analytics dashboard and is gradually evolving into a fully AI-powered analytics platform capable of supporting natural-language analytics, AI agents, and intelligent business insights.

---

## Dataset

Records: 9,289+

Key Fields:

- Program
- Academic Year
- Funding Source
- State
- Placement Information
- Package Amount
- Completion Status
- Career Center

---

## Features

### Executive Dashboard

- Total Students
- Completed Students
- Placed Students
- Revenue Metrics
- Enrollment Trends
- State Performance Analytics

### Program Analytics

- Program Enrollment
- Completion Rate
- Placement Rate
- Revenue by Program
- Average Training Duration

### Placement Analytics

- Placement Performance
- Top Employers
- Salary Distribution
- Program Placement Comparison

### Funding Analytics

- Funding Source Performance
- Revenue Analysis
- Completion Rate by Funding Source
- Placement Rate by Funding Source

### Career Center Analytics

- Career Center Performance
- Coordinator Performance
- Student Distribution
- Completion and Placement Outcomes

### AI Assistant

The AI Assistant provides a natural-language analytics interface that translates business questions into SQL-driven insights.

Supported questions include:

- total students
- placement rate
- completion rate
- students by state
- top employers
- largest program
- largest state
- largest funding source
- revenue by program
- placement by state
- completion by state

The current version uses a rule-based query engine and serves as the foundation for future AI-powered SQL generation.

---

## FastAPI Backend

Version 1.0 includes a FastAPI backend that exposes analytics data through REST APIs.

Current functionality includes:

### API Endpoints

#### General