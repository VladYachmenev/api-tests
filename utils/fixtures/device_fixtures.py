import pytest
from api.clients.base_clients import HttpClient
from api.clients.device_client import DeviceApiClient
from utils.factories.device_factory import generate_full_payload


@pytest.fixture(scope='class')
def class_devices_api() -> DeviceApiClient:
    http_client: HttpClient = HttpClient()
    device_api = DeviceApiClient(client=http_client)
    yield device_api
    device_api.client.session.close()


@pytest.fixture(scope='function')
def function_create_device_api(class_devices_api: DeviceApiClient):
    payload = generate_full_payload()
    response = class_devices_api.create_devices_api(payload.model_dump(by_alias=True))
    yield response.json()['id']
    class_devices_api.delete_device_api(response.json()['id'])
