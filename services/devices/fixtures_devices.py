import pytest
from shared.clients import HttpClient
from services.devices.api_devices import DevicesApi


@pytest.fixture(scope='function')
def function_devices_api() -> DevicesApi:
    client: HttpClient = HttpClient()
    return DevicesApi(client=client)