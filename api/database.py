import sqlite3


def get_connection():

    conn = sqlite3.connect(
        "database/training_analytics.db",
        check_same_thread=False
    )

    return conn