import pytest
from api.clients.base_clients import HttpClient
from api.clients.device_client import DeviceApiClient
from utils.factories.device_factory import generate_full_payload


@pytest.fixture(scope='function')
def function_devices_api() -> DeviceApiClient:
    client: HttpClient = HttpClient()
    return DeviceApiClient(client=client)


@pytest.fixture(scope='function')
def function_create_device_api(function_devices_api: DeviceApiClient):
    payload = generate_full_payload()
    response = function_devices_api.create_devices_api(payload.model_dump(by_alias=True))
    yield response.json()['id']
    function_devices_api.delete_device_api(response.json()['id'])
