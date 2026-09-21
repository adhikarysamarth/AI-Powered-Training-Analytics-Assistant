import requests


BASE_URL = "http://127.0.0.1:8000"


def get_program_summary():

    response = requests.get(
        f"{BASE_URL}/program_summary"
    )

    return response.json()


def get_state_summary():

    response = requests.get(
        f"{BASE_URL}/state_summary"
    )

    return response.json()


def get_funding_summary():

    response = requests.get(
        f"{BASE_URL}/funding_summary"
    )

    return response.json()