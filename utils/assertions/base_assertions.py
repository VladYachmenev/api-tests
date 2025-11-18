from requests import Response


def validate_schema(instance: Response, model):
    return model(**instance.json())


def validate_scheme_for_array(instance: Response, model):
    return [model(**item) for item in instance.json()]


def assert_status_code(response: Response, expected_code: int) -> None:
    assert response.status_code == expected_code, (
        f"Expected status code {expected_code}, but got {response.status_code}. "
        f"Response: {response.text}"
    )