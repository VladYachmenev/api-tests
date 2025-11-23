from requests import Response
from pydantic import ValidationError
import allure


@allure.step('Validating schema')
def validate_schema(instance: dict, model):
    try:
        return model(**instance)
    except ValidationError:
        raise


@allure.step('Validating schema')
def validate_scheme_for_array(instance: dict, model):
    try:
        return [model(**item) for item in instance]
    except ValidationError:
        raise


@allure.step('Validating status code')
def assert_status_code(response: Response, expected_code: int) -> None:
    assert response.status_code == expected_code, (
        f"Expected status code {expected_code}, but got {response.status_code}. "
        f"Response: {response.text}"
    )
