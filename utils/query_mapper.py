QUERY_MAP = {

    "total students": """
    SELECT COUNT(*) AS TotalStudents
    FROM training_data
    """,

    "placement rate": """
    SELECT
        Program,
        ROUND(AVG(Placed) * 100, 2) AS PlacementRate
    FROM training_data
    GROUP BY Program
    ORDER BY PlacementRate DESC
    """,

    "completion rate": """
    SELECT
        Program,
        ROUND(AVG(Completed) * 100, 2) AS CompletionRate
    FROM training_data
    GROUP BY Program
    ORDER BY CompletionRate DESC
    """,

    "students by state": """
    SELECT
        State,
        COUNT(*) AS Students
    FROM training_data
    GROUP BY State
    ORDER BY Students DESC
    """,

    "top employers": """
    SELECT
        "Placement Employer" AS Employer,
        COUNT(*) AS Hires
    FROM training_data
    WHERE Placed = 1
    GROUP BY "Placement Employer"
    ORDER BY Hires DESC
    LIMIT 10
    """,

    "largest program": """
    SELECT
        Program,
        COUNT(*) AS Students
    FROM training_data
    GROUP BY Program
    ORDER BY Students DESC
    LIMIT 1
    """,

    "largest state": """
    SELECT
        State,
        COUNT(*) AS Students
    FROM training_data
    GROUP BY State
    ORDER BY Students DESC
    LIMIT 1
    """,

    "largest funding source": """
    SELECT
        "Training Program Funding Source" AS FundingSource,
        COUNT(*) AS Students
    FROM training_data
    GROUP BY "Training Program Funding Source"
    ORDER BY Students DESC
    LIMIT 1
    """,

    "revenue by program": """
    SELECT
        Program,
        SUM("Package Amount") AS Revenue
    FROM training_data
    GROUP BY Program
    ORDER BY Revenue DESC
    """,

    "placement by state": """
    SELECT
        State,
        ROUND(AVG(Placed) * 100,2) AS PlacementRate
    FROM training_data
    GROUP BY State
    ORDER BY PlacementRate DESC
    """,

    "completion by state": """
    SELECT
        State,
        ROUND(AVG(Completed) * 100,2) AS CompletionRate
    FROM training_data
    GROUP BY State
    ORDER BY CompletionRate DESC
    """,

    "students by coordinator": """
    SELECT
        Coordinator,
        COUNT(*) AS Students
    FROM training_data
    GROUP BY Coordinator
    ORDER BY Students DESC
    """,

    "students by funding source": """
    SELECT
        "Training Program Funding Source" AS FundingSource,
        COUNT(*) AS Students
    FROM training_data
    GROUP BY "Training Program Funding Source"
    ORDER BY Students DESC
    """,

    "top career centers": """
    SELECT
        "Assigned Career center" AS CareerCenter,
        COUNT(*) AS Students
    FROM training_data
    GROUP BY "Assigned Career center"
    ORDER BY Students DESC
    LIMIT 10
    """,

    "highest placement program": """
    SELECT
        Program,
        ROUND(AVG(Placed) * 100,2) AS PlacementRate
    FROM training_data
    GROUP BY Program
    ORDER BY PlacementRate DESC
    LIMIT 1
    """,

    "highest completion program": """
    SELECT
        Program,
        ROUND(AVG(Completed) * 100,2) AS CompletionRate
    FROM training_data
    GROUP BY Program
    ORDER BY CompletionRate DESC
    LIMIT 1
    """,

    "average training duration": """
    SELECT
        ROUND(AVG("Training Duration Days"),0)
        AS AverageTrainingDays
    FROM training_data
    """,

    "placement salary ranges": """
    SELECT
        "Placement Salary Range",
        COUNT(*) AS Students
    FROM training_data
    WHERE Placed = 1
    GROUP BY "Placement Salary Range"
    ORDER BY Students DESC
    """,

    "sql students": """
    SELECT
        COUNT(*) AS Students
    FROM training_data
    WHERE Program LIKE '%SQL%'
    """,

    "sql placement rate": """
    SELECT
        ROUND(AVG(Placed) * 100,2)
        AS PlacementRate
    FROM training_data
    WHERE Program LIKE '%SQL%'
    """,

    "sql completion rate": """
    SELECT
        ROUND(AVG(Completed) * 100,2)
        AS CompletionRate
    FROM training_data
    WHERE Program LIKE '%SQL%'
    """,

    "sql completion rate": """
    SELECT
        ROUND(AVG(Completed) * 100,2)
        AS CompletionRate
    FROM training_data
    WHERE Program LIKE '%SQL%'
    """
}