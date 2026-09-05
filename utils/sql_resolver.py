def resolve_question(question):

    question = question.lower()

    if "placement" in question:

        return """
        SELECT
            Program,
            PlacementRate
        FROM program_summary
        ORDER BY PlacementRate DESC
        """

    elif "completion" in question:

        return """
        SELECT
            Program,
            CompletionRate
        FROM program_summary
        ORDER BY CompletionRate DESC
        """

    elif "state" in question:

        return """
        SELECT *
        FROM state_summary
        ORDER BY TotalStudents DESC
        """

    elif "funding" in question:

        return """
        SELECT *
        FROM funding_summary
        ORDER BY TotalStudents DESC
        """

    return None