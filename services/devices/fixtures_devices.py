import pytest
from shared.clients import HttpClient
from services.devices.api_devices import DevicesApi
from services.devices.factories import generate_device_data


@pytest.fixture(scope='function')
def function_devices_api() -> DevicesApi:
    client: HttpClient = HttpClient()
    return DevicesApi(client=client)


@pytest.fixture(scope='function')
def function_create_device_api(function_devices_api):
    payload = generate_device_data()
    response = function_devices_api.create_devices_api(payload.model_dump(by_alias=True))
    yield response.json()['id']
    function_devices_api.delete_device_api(response.json()['id'])
