from pydantic import ValidationError
from requests import Response
from pydantic import BaseModel


def validate_schema(instance: dict, model):
    return model(**instance)


def validate_scheme_for_array(instance, model):
    return [model(**item) for item in instance]


def assert_status_code(response: Response, expected_code: int) -> None:
    assert response.status_code == expected_code, (
        f"Expected status code {expected_code}, but got {response.status_code}. "
        f"Response: {response.text}"
    )
