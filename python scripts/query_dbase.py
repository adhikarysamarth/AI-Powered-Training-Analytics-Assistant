import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "database/training_analytics.db"
)

query = """
SELECT *
FROM program_summary
ORDER BY PlacementRate DESC
"""

result = pd.read_sql(query, conn)

print(result)