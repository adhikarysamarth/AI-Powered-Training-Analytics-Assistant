-- Program Summary View

CREATE VIEW IF NOT EXISTS program_summary AS
SELECT
    Program,
    COUNT(*) AS TotalStudents,
    ROUND(AVG(Completed)*100,2) AS CompletionRate,
    ROUND(AVG(Placed)*100,2) AS PlacementRate,
    SUM("Package Amount") AS Revenue,
    ROUND(AVG("Training Duration Days"),0) AS AvgTrainingDays
FROM training_data
GROUP BY Program;


-- State Summary View

CREATE VIEW IF NOT EXISTS state_summary AS
SELECT
    State,
    COUNT(*) AS TotalStudents,
    ROUND(AVG(Completed)*100,2) AS CompletionRate,
    ROUND(AVG(Placed)*100,2) AS PlacementRate
FROM training_data
GROUP BY State;

-- Career Center View

CREATE VIEW IF NOT EXISTS career_center_summary AS

SELECT
    "Assigned Career center" AS CareerCenter,
    COUNT(*) AS TotalStudents,
    ROUND(AVG(Completed)*100,2) AS CompletionRate,
    ROUND(AVG(Placed)*100,2) AS PlacementRate
FROM training_data
GROUP BY "Assigned Career center";

-- Funding Summary View

CREATE VIEW IF NOT EXISTS funding_summary AS
SELECT
    "Training Program Funding Source" AS FundingSource,
    COUNT(*) AS TotalStudents,
    ROUND(AVG(Completed)*100,2) AS CompletionRate,
    ROUND(AVG(Placed)*100,2) AS PlacementRate,
    SUM("Package Amount") AS Revenue
FROM training_data
GROUP BY "Training Program Funding Source";


-- Coordinator Summary View

CREATE VIEW IF NOT EXISTS coordinator_summary AS
SELECT
    Coordinator,
    COUNT(*) AS TotalStudents,
    ROUND(AVG(Completed)*100,2) AS CompletionRate,
    ROUND(AVG(Placed)*100,2) AS PlacementRate
FROM training_data
GROUP BY Coordinator;