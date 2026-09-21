import sqlite3


def get_connection():

    connection = sqlite3.connect(
        "database/training_analytics.db",
        check_same_thread=False
    )

    return connection