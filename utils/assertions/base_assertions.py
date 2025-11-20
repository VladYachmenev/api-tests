from requests import Response
from pydantic import ValidationError


def validate_schema(instance: Response, model):
    try:
        return model(**instance.json())
    except ValidationError:
        raise


def validate_scheme_for_array(instance: Response, model):
    try:
        return [model(**item) for item in instance.json()]
    except ValidationError:
        raise


def assert_status_code(response: Response, expected_code: int) -> None:
    assert response.status_code == expected_code, (
        f"Expected status code {expected_code}, but got {response.status_code}. "
        f"Response: {response.text}"
    )
