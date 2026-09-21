import requests

BASE_URL = "http://127.0.0.1:8000"


def get_total_students():

    response = requests.get(
        f"{BASE_URL}/students",
        timeout=10
    )

    response.raise_for_status()

    return response.json()


def get_program_summary():

    response = requests.get(
        f"{BASE_URL}/program_summary",
        timeout=10
    )

    response.raise_for_status()

    return response.json()


def get_state_summary():

    response = requests.get(
        f"{BASE_URL}/state_summary",
        timeout=10
    )

    response.raise_for_status()

    return response.json()


def get_funding_summary():

    response = requests.get(
        f"{BASE_URL}/funding_summary",
        timeout=10
    )

    response.raise_for_status()

    return response.json()


def ask_question(question):

    response = requests.post(
        f"{BASE_URL}/question",
        json={
            "question": question
        },
        timeout=30
    )

    response.raise_for_status()

    return response.json()