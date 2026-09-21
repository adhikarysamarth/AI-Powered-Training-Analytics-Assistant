def resolve_question(question):

    question = question.lower().strip()

    # Total students
    if "total students" in question:

        return """
        SELECT
            COUNT(*) AS TotalStudents
        FROM training_data
        """

    # Students by state
    elif "students by state" in question:

        return """
        SELECT
            State,
            COUNT(*) AS Students
        FROM training_data
        WHERE State IS NOT NULL
        GROUP BY State
        ORDER BY Students DESC
        """

    # Placement rate
    elif "placement rate" in question:

        return """
        SELECT
            Program,
            ROUND(AVG(Placed) * 100, 2) AS PlacementRate
        FROM training_data
        WHERE Program IS NOT NULL
        GROUP BY Program
        ORDER BY PlacementRate DESC
        """

    # Completion rate
    elif "completion rate" in question:

        return """
        SELECT
            Program,
            ROUND(AVG(Completed) * 100, 2) AS CompletionRate
        FROM training_data
        WHERE Program IS NOT NULL
        GROUP BY Program
        ORDER BY CompletionRate DESC
        """

    # Funding source
    elif "funding source" in question:

        return """
        SELECT
            "Training Program Funding Source" AS FundingSource,
            COUNT(*) AS Students
        FROM training_data
        WHERE "Training Program Funding Source" IS NOT NULL
        GROUP BY "Training Program Funding Source"
        ORDER BY Students DESC
        """

    # Top employers
    elif "top employers" in question:

        return """
        SELECT
            "Placement Employer" AS Employer,
            COUNT(*) AS Hires
        FROM training_data
        WHERE Placed = 1
          AND "Placement Employer" IS NOT NULL
        GROUP BY "Placement Employer"
        ORDER BY Hires DESC
        LIMIT 10
        """

    # Largest program
    elif "largest program" in question:

        return """
        SELECT
            Program,
            COUNT(*) AS Students
        FROM training_data
        WHERE Program IS NOT NULL
        GROUP BY Program
        ORDER BY Students DESC
        LIMIT 1
        """

    # Largest state
    elif "largest state" in question:

        return """
        SELECT
            State,
            COUNT(*) AS Students
        FROM training_data
        WHERE State IS NOT NULL
        GROUP BY State
        ORDER BY Students DESC
        LIMIT 1
        """

    # Revenue by program
    elif "revenue by program" in question:

        return """
        SELECT
            Program,
            ROUND(SUM("Package Amount"), 2) AS Revenue
        FROM training_data
        WHERE Program IS NOT NULL
        GROUP BY Program
        ORDER BY Revenue DESC
        """

    # Placement by state
    elif "placement by state" in question:

        return """
        SELECT
            State,
            ROUND(AVG(Placed) * 100, 2) AS PlacementRate
        FROM training_data
        WHERE State IS NOT NULL
        GROUP BY State
        ORDER BY PlacementRate DESC
        """

    # Completion by state
    elif "completion by state" in question:

        return """
        SELECT
            State,
            ROUND(AVG(Completed) * 100, 2) AS CompletionRate
        FROM training_data
        WHERE State IS NOT NULL
        GROUP BY State
        ORDER BY CompletionRate DESC
        """

    return None