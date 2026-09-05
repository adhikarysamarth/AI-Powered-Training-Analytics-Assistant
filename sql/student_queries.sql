-- Total Students

SELECT COUNT(*) AS TotalStudents
FROM training_data;


-- Students by Program

SELECT
    Program,
    COUNT(*) AS StudentCount
FROM training_data
GROUP BY Program
ORDER BY StudentCount DESC;

-- Students by Academic Year

SELECT
    "Academic Year",
    COUNT(*) AS StudentCount
FROM training_data
GROUP BY "Academic Year"
ORDER BY "Academic Year";

-- Students by State

SELECT
    State,
    COUNT(*) AS StudentCount
FROM training_data
GROUP BY State
ORDER BY StudentCount DESC;


-- Students by Gender

SELECT
    Gender,
    COUNT(*) AS StudentCount
FROM training_data
GROUP BY Gender;

-- Most Popular Programs

SELECT
    Program,
    COUNT(*) AS Enrollments
FROM training_data
GROUP BY Program
ORDER BY Enrollments DESC;


-- Revenue by Program

SELECT
    Program,
    SUM("Package Amount") AS Revenue
FROM training_data
GROUP BY Program
ORDER BY Revenue DESC;


-- Average Package Amount by Program

SELECT
    Program,
    ROUND(AVG("Package Amount"), 2) AS AvgTuition
FROM training_data
GROUP BY Program
ORDER BY AvgTuition DESC;

-- Students by Funding Source

SELECT
    "Training Program Funding Source",
    COUNT(*) AS StudentCount
FROM training_data
GROUP BY "Training Program Funding Source"
ORDER BY StudentCount DESC;


-- Revenue by Funding Source

SELECT
    "Training Program Funding Source",
    ROUND(SUM("Package Amount") / 1000, 2) AS 'Revenue (in Thousands)'
FROM training_data
GROUP BY "Training Program Funding Source"
ORDER BY 'Revenue (in Thousands)' DESC;

PRAGMA table_info(training_data);